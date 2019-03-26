import openapi_server.static_vars as StaticVars

def obtain_uri(id):
    #todo: magic
    return StaticVars.DEFAULT_MINT_INSTANCE + id
