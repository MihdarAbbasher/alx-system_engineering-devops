reame for 0x10-https_ssl

0. World wide web
go to .tech web site and add the record pointing to IPs

1. HAproxy SSL termination:
login to every server using ssh command
ssh -i private_key_path user@server

configure:
	sudo apt update
	sudo install snapd
	sudo apt-get remove certbot
	sudo apt-get install certbot
	sudo cerbot certonly --standalone -- preferred-challenges http --http-01-prt 80 -d domain_name
