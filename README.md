# forti-backup

howto backup a fortinet appliance ?

you need an IP:PORT and a TOKEN ..

environment

  * ip:port off appliance, required via FORTI_APPLIANCE
  * token to access, required via FORTI_TOKEN
  * product type, default "fortinet", optional, FORTI_PRODUCT
  * scope, default "global", optional, FORTI_SCOPE

hint

  * make sure the API User has "write" access for "system"
