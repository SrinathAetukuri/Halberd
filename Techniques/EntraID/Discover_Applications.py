#Discover Applications
from core.GraphFunctions import graph_get_request
from dash import html

def TechniqueMain():
    endpoint_url = "https://graph.microsoft.com/v1.0/applications/"

    tenant_applications = graph_get_request(url = endpoint_url)
    print("Tenant apps found")
    
    return tenant_applications


def TechniqueInputSrc() -> list:
    '''Returns the input fields required as parameters for the technique execution'''
    return []