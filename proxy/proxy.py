from attr import attrs,attrib


@attrs
class Proxy:
    host = attrib(type=str,default='0')
    port =  attrib(type=int,default=0)

    def __str__(self) -> str:
        return f"{self.host}:{self.port}"