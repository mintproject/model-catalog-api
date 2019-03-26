import openapi_server.static_vars as staticvars

def obtain_uri(id):
    #todo: magic
    return staticvars.DEFAULT_MINT_INSTANCE + id
