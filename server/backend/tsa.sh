# ===========================================================================
# \brief Запрос и ответ TSA = TimeStamp Authority
# \project bpki/demo
# \created 2018.01.10
# \version 2018.01.23
# \pre Выполнен скрипт setup.sh.
# \#ark ТSA = СШВ = Служба штампов времени
# \#ark Выпускаются две пары "запрос - ответ": лаконичная и подробная.
# В лаконичной паре заблокированы нонсы, сертификат TSA не включается в 
# ответ. В подробной паре все наоборот.
# \#ark Ответ TSA представляет собой контейнер с двумя полями: 
#   - cтатус обработки,
#   - штамп времени -- контейнер типа SignedData. 
# Штамп времени как SignedData включает 4 подписанных атрибута: contentType, 
# MessageDigest, SigningCertificate, SigningTime. 
# Первые два атрибута # обязательны по правилам СТБ 34.101.23-cms. 
# Третий атрибут описывает описывает хэш-значение сертификата TSA. 
# Четвертый атрибут имеет мало смысла (время уже указано в штампе),
# но подавить его через командную строку нельзя.
# \warning В текущей редакции СТБ 34.101.ts требуется использовать не 
# SigningCertificate, а SigningCertificateV2.
# ===========================================================================

echo "== Testing TSA Services =================================================="

export OPENSSL_CONF=openssl.cfg
mkdir out 2> /dev/null
cat out/ca1/cert out/tsa/cert | tee -a out/tsa/chain> /dev/null

echo "-- 1 TSA Request1 ---------------------"

openssl ts -query -data tsa.sh -bash256 -out out/tsa/req1.tsq -no_nonce 2> /dev/null

# dumpasn1b -z -cdumpasn1by.cfg out/tsa/req1.tsq out/tsa/req1.txt 2> nul

# echo stored in out/tsa/req1.tsq

echo "-- 2 TSA Response1 --------------------"

openssl ts -reply -queryfile out/tsa/req1.tsq \
  -signer out/tsa/cert -passin pass:tsatsatsa -inkey out/tsa/privkey \
  -out out/tsa/resp1.tsr -no_nonce 2> /dev/null

# dumpasn1b -z -cdumpasn1by.cfg out/tsa/resp1.tsr out/tsa/resp1.txt 2> nul

# echo stored in out/tsa/resp1.tsr

echo "-- 3 TSA Verify1 ----------------------"

openssl ts -verify -queryfile out/tsa/req1.tsq -in out/tsa/resp1.tsr \
  -CAfile out/ca0/cert -untrusted out/tsa/chain 2> /dev/null

echo "-- 4 TSA Request2 ---------------------"

openssl ts -query -data tsa.sh -bash512 -out out/tsa/req2.tsq -cert > /dev/null

# dumpasn1b -z -cdumpasn1by.cfg out/tsa/req2.tsq out/tsa/req2.txt 2> nul

# echo stored in out/tsa/req2.tsq

echo "-- 5 TSA Response2 --------------------"

openssl ts -reply -queryfile out/tsa/req2.tsq \
  -signer out/tsa/cert -passin pass:tsatsatsa -inkey out/tsa/privkey \
  -out out/tsa/resp2.tsr 2> /dev/null

# dumpasn1b -z -cdumpasn1by.cfg out/tsa/resp2.tsr out/tsa/resp2.txt 2> nul

# echo stored in out/tsa/resp2.tsr

echo "-- 6 TSA Verify2 ----------------------"

openssl ts -verify -data tsa.sh -bash512 -in out/tsa/resp2.tsr \
  -CAfile out/ca0/cert -untrusted out/ca1/cert 2> /dev/null

openssl ts -verify -queryfile out/tsa/req2.tsq -in out/tsa/resp2.tsr \
  -CAfile out/ca0/cert -untrusted out/ca1/cert 2> /dev/null

echo "== End ==================================================================="
