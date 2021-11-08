workspace {

    model {
        user = person "User"

        authSystem = softwareSystem "Authentication" {
            authDatabase = container "Database"
            keycloak = container "Keycloak"
        }

        modelCatalogSystem = softwareSystem "ModelCatalog" {
            database = container "Database"
            api = container "Model Catalog API" {
                -> database "Makes a SPARQL query"
            }
            ui = container "UI" {
                -> api "Send HTTP request"
            }
            database -> api "Returns a JSON/LD"
            api -> ui "Returns a JSON matching the OpenAPI spec"
            ui -> keycloak "Send user and password"
            keycloak -> ui "Send JWT token"
            api -> keycloak "If POST/PUT/DELETE, then verify JWT Token"
        }
        
        user -> ui "Get, create, update or delete models"
        ui -> user "Display models or changes" 
        
        
        deploymentEnvironment "Production" {
            deploymentNode "Docker - Polymer" {
                containerInstance ui
            }
            deploymentNode "Docker - SPARQL mintproject/fuseki-docker"  {
                containerInstance database 
            }
            deploymentNode "Docker Python - mintproject/model-catalog-api"  {
                containerInstance api
            }
            deploymentNode "Docker Keycloak - mintproject/installation-public"  {
                containerInstance keycloak
            }
        }


    }

    views {
    
       container modelCatalogSystem "Containers" {
            include *
            autoLayout
        }
    
        systemlandscape "SystemLandscape" {
            include *
            autoLayout lr
        }
        
        
        deployment modelCatalogSystem "Production" {
            include *
            autolayout  lr
        }


    }

}