#!/bin/bash
echo "== Creating End Entity $1"
cd out
mkdir $1 2> /dev/null
cd ..

openssl genpkey -paramfile out/params256 -out out/$1/privkey_plain

#call decode out/%1/privkey_plain > nul#

openssl pkcs8 -in out/$1/privkey_plain -topk8 \
  -v2 belt-kwp256 -v2prf belt-hmac -iter 10000 \
  -passout pass:$1$1$1 -out out/$1/privkey

#call decode out/%1/privkey > nul#

openssl req -new -utf8 -nameopt multiline,utf8 -config ./cfg/$1.cfg \
  -reqexts reqexts -key out/$1/privkey -passin pass:$1$1$1 \
  -out out/$1/csr -batch

#if %ERRORLEVEL% neq 0 goto Create_Error#

#call decode out/%1/csr > nul#

openssl ca -name ca1 -batch -in out/$1/csr -key ca1ca1ca1 -days $2 \
  -extfile ./cfg/$1.cfg -extensions exts -out out/$1/cert -notext \
  -utf8 2> /dev/null

#if %ERRORLEVEL% neq 0 goto Create_Error#

#call decode out/%1/cert > nul#

#echo Creating %1... ok#

#goto Create_End#

#:Create_Error
#echo Creating %1... Failed
#exit /b 1#

#:Create_End
#exit /b 0#