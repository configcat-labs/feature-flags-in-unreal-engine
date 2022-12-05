import unreal
import configcatclient

configcat_client = configcatclient.create_client('YOUR_CONFIGCAT_SDK_KEY')

dialogmessage = configcat_client.get_value('dialogmessage', False)

if dialogmessage:
  unreal.EditorDialog.show_message("Feature flag status", "This message is shown because your feature flag is enabled in ConfigCat!", unreal.AppMsgType.OK)

print('dialogmessage\'s value from ConfigCat: ' + str(dialogmessage))
