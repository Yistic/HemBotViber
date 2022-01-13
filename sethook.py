from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

viber = Api(BotConfiguration(
    name='MEEhem',
    avatar='https://dl-media.viber.com/1/share/2/long/vibes/icon/image/0x0/49b0/390b4c4b55c07209d0e300ce06736c93943c9f036141ef57272aeacfb54a49b0.jpg',
    auth_token='4ae98f9cd767d2a3-407ff423b15ea797-2f9575a149ee9956'
))
viber.set_webhook('https://25e8-87-116-161-50.ngrok.io/')