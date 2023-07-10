# -*- coding: utf-8 -*-
from atramhasis import skos

from skosprovider.registry import Registry
from skosprovider.uri import UriPatternGenerator
from skosprovider_sqlalchemy.providers import SQLAlchemyProvider

import logging
log = logging.getLogger(__name__)


def create_registry(request):
    # create the SKOS registry
    registry = Registry(instance_scope='threaded_thread')
    skos.register_providers_from_db(registry, request.db)

    # create your own providers
    #
    # TREES = SQLAlchemyProvider(
    #     {'id': 'TREES', 'conceptscheme_id': 1},
    #     request.db
    # )
    
    # Add your custom provider to the registry
    # registry.register_provider(TREES)

    # return the SKOS registry
    return registry
