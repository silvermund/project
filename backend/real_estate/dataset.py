from dataclasses import dataclass


@dataclass
class Dataset(object):

    context: str
    fname: str
    housing: object