sudo docker run -it --rm -p 80:80 --name certbot \
                -v "/etc/letsencrypt:/etc/letsencrypt" \
                -v "/var/lib/letsencrypt:/var/lib/letsencrypt"  \
                certbot/certbot:arm32v6-nightly certonly  \
                --standalone   \
                --email uriel.arriaga@momodevops.dev \
                -d depa-dnkrvqmqhr.dynamic-m.com
