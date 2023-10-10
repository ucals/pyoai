from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader


def test_missing_datetime():
    arxiv_id = '2310.04421'
    registry = MetadataRegistry()
    registry.registerReader('oai_dc', oai_dc_reader)
    client = Client('http://export.arxiv.org/oai2', registry)
    kwargs = {
        'metadataPrefix': 'oai_dc',
        f'identifier': f'oai:arXiv.org:{arxiv_id}'
    }
    data = client.getRecord(**kwargs)
    final = data[1].getMap()
    print(final)
