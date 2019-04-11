export RESTFULGIT_CONFIG=/root/restfulgit/myconfig.py
exec python restfulgit/app.py >> log.restfulgit.log 2>&1 
# supervisord conf
# [program:app]
# command=sh run.sh
# directory=/root/restfulgit
# user=root
# autostart=true
# autorestart=true
