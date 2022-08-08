from managers.auth import AuthManager


def generate_token(user):
    token = AuthManager.encode_token(user)
    return token


def mock_uuid():
    return "1111-1111-1111-1111"


encoded_photo = "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCADIAMgDAREAAhEBAxEB/8QAHQAAAQMFAQAAAAAAAAAAAAAAAgUHCAEDBAYJAP/EAEMQAAECBAQDBgQDBQYFBQAAAAECAwAEBREGEiExB0FRCBMiYXGBFJGhsQkyQhUjUsHwFiQzctHhFyVigvE0NkNTkv/EABsBAAEFAQEAAAAAAAAAAAAAAAABAgMEBQYH/8QALBEAAgICAgEFAAIBBAMBAAAAAAECEQMhBBIxBRMiQVEjMmEzQnGBBhQkof/aAAwDAQACEQMRAD8AmeNopF0MbQAVG8ABQAEDygBhjaAagxtAODG0ABAQCMICAQrAB6AVHoBT0AjPQAimWEFAywjAEi8IBQi0AFIAAUnWAASIABItAAKheAC2oWgAqN4ACgAqDygArAAQPKAAgeUKgLg2hQCBgAuJF4ACgAICBgVhoFCLwAeywAeywAUItABSACmWAASLwAAReAChFoABULwABlgAEiAAFC8AFuACoPKACt9bQAEDaACo1gAIHlAAaTaAC4DABcQbwAXALwAGmAAoAPQCnoABywCHssAAkXgAoRaACkAFCmAC2RDWBTLCoAYRgApMIABEAFiHilCYBDwMApUGAAgrWAAgYADBgAuJOkAFxJgAMuJbGYqsB1MAqVjScTu1bw+4WNLTPVUVGfBIElT7OLv5m9k+5g39CtUMdMfiV0gzBTL4Sd7rWy3p0A36WCTCNSC4HpP8S2lFxSZnCDqcguvu50Xt5XTCVJB8H9m+YX/EG4YV5CfjFz9HduMyX2c4HndPKEtryFR+mPtgziRhniDJiZw9XJOqotcpYdBWn1TuPcQqkgaNksIcMKQCgkQ1iA5YQChFoAKEXgAApgAAiAAbQACpMAGEd4VDmUhwiPQDiu0ABA84ACBvAAY2gAMG0AFudqMvTJR2ZmnUMMNJKluLNgkDckmEboErOeva+7an9pUu4WwdOqZpqFlMzPsqIL5H6Un+Hz5wm2PclBbIVzGIZuYUsuTCpjObkq3iVKiByswfjVury7BWlxpCt0NqzL7icZfbzrsCncncQnaxetFt9yZZWO7KuhIhLX2LT+hUw3juv4Qq0vUaJPTUjOtKCkvsOqSUkekMajJgpSROLgd+JoW22KXxHpi3imyP2vTUajzcbvr6p+UNpoemmTewRxSwrxGpzc7hytylUYWL/uV+JPkpJ1B9YLTBpm02BgGlLQACU6QACUwADAAJEAAqFoALZgAT4B56FQHoVgVtDQCG0AFQNYADG8AAvPJYaU4o2AF7wBTfg5q9tbtVzeLcQz2EsPThbocmosTDrS7CYWPzD/KDp52hyVkjftqiGjr6n3M615iYnjoqSfZmfTKUucdSR4E33G8EvFiximKE3IGRnLqSEtDYKOp9RELfZWSKPVgzZ+JQVN3NlAgHWCGkE9svLL0qUtOBKFgeHMNxvAqlsP66MFVR7hjKQkBRII5iHdFZF2aZfNRk5SVCglJXslPnCdG2SdkkbXwQ4vVbhDxGpVelJl5DaXgJlhJORxo6KSRz02hMkUlaEg3dM7W4MxLK4uw5T6vJL7yVnGEPNnqlQuLxGnaHtUxchRpTLAAJEAAqTrAAJFoABIvABbUmABM3gHntoAKjUwAEBygAK1oAKgXgA8vwp0384AIqduXtDnhfg5OHKRMFOIqy2pAUg+KXY2UvyJ2HuYFslSpWcuJ1z4hZWtSlEndR1JiZKiCT7FtEuF/4hCR0hzdEdWbNRluSSM5byt+oF4Y5Wh8Y1sV5ejVLH75EjIqKG9O9vZPzMVXNQW2Wlilk8I3Oi9nfEj6GymWEw2vYIPi/2ipPnQWi3D07J/YdSmdlCsVOlMt1FtKHU6oKj40j+E+UZz9QUXo0IcHstoRsTdlBFOQ8onxpbvkSSbKHn5wsPUrY6XpioYjE/DqYoU6W3WFKCNbbWF9418fKU15MjLw3B+C21SG3GEhSQlSdlJVcj15xY9y9MquHU6e9grHaq9wdbpb5K5mjOmXNzchs6p/nDIu20ElWyUiSFpCgbg7RIRMpAIeIvAABEAAEQADAAKhpAKJMA49AAQEABgQAVAvAAW0AGDW6kzR6XMz0wsIYl0KcWo7AAXJgHxVujjDx74mTXFXifXK++4pxp54tyySf8NlJshI9tfeCGiSap0N0looXcgqdOwH6R0iZFZixTKOpSkvLAPQqOntA5JCKLkx0OG/CuYxtOWX4pdKgCOQ12jJz5+ps8Xi91bJncN+BNNpdMYbcCcoVcoRtv9/OOfy5py22dJjxQgqSHzoeDKbT27oYQlRG1rW8hFFtvyTpUK85TmEgfu066ADQRE4kiNKxNhdh9ogixOuW+l/OGO14J0iOnFPhjLfHuuBgKQtktg+e4i7hzSRWzYYy+iJFelhRamplScjZVp1T6R1eBucU2cbyYe3Nokv2E+IjuHOJS6KSky9UZIKCbEqSLpsfS8Sr4zIWrgdIpR0OsoWghSFC4MWSm0ZBN4BCkAh4i8AAEQAAoawjAEi4hByEeHChAQAGBAAQEAFdoAK2vABH/ts8R04A4JVNttwCdqn9yaF7Gyh4iPQfeGy/CziW7OTDqlJvtnOpJ5Q/6FfyZbC0tupCR3ryv1OC4HnaJFsry+JtlNl3FqaObvHV2sOnT/xEU3okxRt0TP4GYMbk5KSlEi4TZb6iP1aaDzjmOTl7SZ2PGxKMEiVVFpzTTacqAlKQAAIpJa2WkqdC42kBQ02iN0voej0zZQuOQhkh60IVZli+jKYqsmTob/GdDE1IvZgLW0vyhFLqDdnPvjuyKRiaZZKbIIK0/wDT/RjtPT32gcV6kqmJPBbGrmHcW0SqoXlck5lChrrlzAKHyi5mVO0Z+J9tHZfB1UE7INuBWZl1CXG1+RF4kj4RDJbZspAIhw0HLAIwYBDxF4BAFCEYpbIhBUI43hwoaRAAYEAFYAK2gA8fCknnAH/Jzb/EU4hit4+p9AbdCpWkMlbiAdC6o/6AQx7kaOOPWFkNG1F5a1qN0J1N+auQiT/BDFXbMmnNgOLcVqbi5P0EP+iB0vkxxMCVCmStYlHam+lloOJWoqF7ARXyQk4uixgyR7JyJqcMuKOB2pJlluuyza1f/arKb+8czl4+RO2jqocrHrqx8qDi+nzbKe4nmJhGgC23Aq/yiNRryWXPttGztVGWcZzB8EDcQ9441YdmJFexrSqDKuPzk0hhhIuVExA8fZ6F7VtjL4g7WlDceXKYfpk5WZm5QgpTkSSOnMxNHiXuRVnyknUTTKjxc4kVR7/2vKpl1DRtSyT7mHy4eOvJGuVO/BFftTOTxm6dU5uSMg5NIUhxm9wlST1941PTYq5QRi+p3UZjQ4UnD3aTcg3jWyx/DIwy/Ts/2WsRjE3C2ivqVnvKNDe/KK8H9E+VVsepAyjrE6KyPHWAUAi8AFIRiMEiEBFtQgFEUehhwFwCAAxtABUbwAVPKFAT8QVRNGpM3Oq1DDSnLdSBeGvwSJW0cT+OeMXsW8QqtOLcLi3X1G/XWExq1bLmZ01BGl3ylDCR+QXVbr0hfOwn8fijPpt1uhlOuupH1MS/RUa7Okbthio4fpLomanLiaAQqyVG5JvZP2itN5JagW8ccUNzN2bx5gmppS07TkSpAsk3KT9Iryw5vssrLgukOTgSsSdByPU+ZmW0qt4VuZhbyPOM3LGS00a2Dr5TJSYFnJqvUgTDa8yct733jOk6s1L14Gm4tYgZamZhuZQqZSxcdyPy384kwpzqiHIqVsj49xjfpdQdkZGkONPoNsjKQ1lB21IJjajxHNeTBy82ON6ibphjidXpDFaKJWZScp825bKiYUFpVcX0UNDFLkcX2Y9kyzx+Ys7pxoye1ngVdT4TftNSCZiVdS9cjWx0P3iH0zPXIr9F9Tw3gbX0Qvw7maV7XIjqsipnLYdnVn8PmuLqHCyVlirOZV5xo6/pvp94ow/s0Xs6+KaJgARZKIJEAAkQACRCMATCAARAAip5Q4C4BABWAAgIAPHaACP/AGzuMEvwn4TTzgc/5nUULk5RF9SpQsVeyb/OEf4WMa2mzkIXlTU65OOnMQSq55q5Q/wqRN/ZubLjKsjS1HVa9deUJ4Yy21YvYSk/iX0oH5l2SPK5tDJyaWh+DH2Zu0nw5empkzqGu8l21pQG1AkK0BP1MVY8rpouPhubscqgcI5Or4hFXmj8GyVJLkqhAUldiCQDfQadLwyXLvaJI+nWPbN4DlZ5ibnWZBMih7UMsoCG7/xWOo9rRQy59WzVxcbolBMd/ga0Kdht+RUSpTaDa/SMLLNybNuMOsUmI1ZwIzV/i1BjO73hdSsbk356bRZ42aviytlxb2rQ1dd4U0+sYmRU6hSVGoJIu7qAq1rXA0OwjRnyJIoS4eGXhDi4L4dtzNaM9PMmYW4b5nk3N/KMjk8iUl1su4ePCHheCz2o6ew3wiryCgBCJc6DyML6c2syKvqCXsyOaLVIMnUHG0gnLce0d7N+Di8MGk2dFvwzp8TOF6yxfVpwLSPUa/URnx/1Wi9nVYosngk3EWjMKkQAAdoABMIwB2hAAVAAjAQ4AxtABWAAhtAB4kBN4BDkl28eLTnEnjI/SpZ7vKVRAZVpKFXSXL3Wr52HtBH9ZcjG0oojm82GsrQ2Rqo9VdIWLt2T5VXxRWxLVzuecBHWtG3cPlpTU0qULpbQVAdYgzWok/GfyomXwRwfL1KgSpm0AulSnVDzUSY5flTkpfE6/jYk4D20rhnTZdaXg0Cb3sYrRzTqqLEuPHzZZxl3dLl0MoCUp84ZOTk9kkcairFPhSkXmnEeJJQUkjUbRA5Xok6ati2Xf2fPpsLKJtlPSI9+UJGP6bGKfJzbQcU0jN1teJrlJeRrUUwXJZmWF02TbbSIvbflg5a0MB2t5xTnCSuSrav3jqEouP8AMI1uBBLMmzD9Qd4miBFIp/ey6Zl2+dSTmv1tHXZJb0YPGx3B2TC/C/qvd4jxNS1K8XcpdSnyCyD9xEGllv8AR3IX/wA//B0aHOJl4Mbzs9CgCRAAJEIwBIhABIuIAEVOtocAUAFRvAAXOADXeIlfGFsDV2qXsZWSedBJ2yoJ/lB4HxXZ0cP5156s1ueqc0czrrqn3Fq5qUb/AM4ZJ/SNbFj/AN30JK7vu2T+W51P1MSKkivL5SaMlUspDOt9RmTCRpsTJD21sXMGOJk5tsqIUouZVeu9h9YXNG0R8aXzROrg9WGWKRLpzBLmUAi/SOTzwuVnc4MiSHvpuI2WkgLOltohjGmWZPsjROJk427MSj7yskln8SidCbaCEmlJ6Fg6WxU4TcT8PScq+18U2heYpUPUxH7NeUNlkfhChO45pNarSpKXdU4+r/DISd79Yryg1sepG0O1xyjBKHiMtt+sTxkmhvksTeK2lsKX3g9jCf2I5SpEde1JXzJcMqjOlJcJeasjNa/iAEafCheVIxedPribIrNN/wBzZAsCoDMLc7Xjbm6kx+LEvZQ/P4eVQ/Z/aHckU2SmZpr+vUgg/wAoPtMyuSv45I6jjUX5RbqjAXg9CCniLwACdIawAO0AAHaABDQdPOHAXBABUbwAFeAVsZftfVddH7P+KyyrI5MMBgEb2UoA/S8MyPrGyxgh2mkcjKo0mXY7kaaZln+UVYNydnQZkscVET6eyHSFFBygxalL6KWOF7M6cIUklZAWr+H9Ih0NIhzruzDk5kSVVkCSUsNuBKhyuSN/p84sTXaJkwft5US3wJU3ZZmXcaVdKgNI5nNGmztMMnVrwOhL4rmklpIFsxtc6AesUJa0jThOvJsNXmWq5RUMoIeINzfUGIYpwlbHPImtGvS2GqO2lV0ttvA3sAL3i/bl4RB8rN4wammSy0vKflGEt2OrgSo26xTy9qqizFNChiXGdMqUwmSac+MKvCVSvjDZ8yNIpe3KKtjZ5G3QlS9KeYyBxRWki9jyiWDdWyGchie17VpJeG5ChfEBMzMPB1LQsSsJNrelzf2jc4MX27/hg86VxWP7bGEavdpBJ05/SLcnbOgUFGEYv8HP7G9VTQ+1nhdtZyJmWnWD5lTagIni7imc3y9TcTrY2ct0nbkYt3bOe+g4AKQjAE+cIABgAA7QAISeUOAujaACo0MABA84BaIadvzi6xSqGxhOWcSuZmx3kxY/4bQIPzURb0B6xUyy7Pqjd9Pwpfyv6OdU2szZWVi2cgwqfRaLUv5Z7KNOAOFCdkC0Klu2RtpaiEtvvC4tV7WslMS3RD07MV8OT0hT259VTlfi5Wbl1NFKfzIXuFp8wbRYg+2jL5mF432HM4JY9bnpISU0sJmGTlIJ+RjL5eKnZq8DOpw6t7JD0idZnKc4w4lK0rHhV5xiSj9m321RomIafNSbpdkpudlZa5Drcs6RY9cvOLGOSqpImwqN1IyMPScqqQ/fTUtOKScwmJtaw5vt4VCLcZqPhGo+Gp1KOVpC8MPUObfQGnHahMr/APgYUUtD26epiplyPyWlCGGDcpWOxhigJo1PbYQwho/nVkTYDyjHy5JTfnRky+XyMfGmMpHCdImqjUZlEuwwgqW4o7RPhg8jUIlHJkWOLlLwQBxjjub4ocR11d0KblWxklmTuhsbX8zuY6+OP/18NfZznGm+XzE34QpSrws6rcixHzil/k7BzuGxd4aVz+yXaMwLVM5QhFQZC1W/SpQB+hiXHqFGBzY/yHaNtWdAvFxO9nMPToLUDrCiFeUI0AJhALajAACjaABDTpDgLo2gAqIBUa1xExlJYFwnUKxPPBmXlmVOKPPQbDzMNm+qJ8WN5ZqKOQfFvG0/xAxRP1ypqUXpx4kIJ0QgbJHoLCKEHdyZ1coLHFY4mgLVmfCddBcmJl8tldutIuSDBeey2tmNvbmYmdFaMW2ZUzZcy42g+BAIuPSG2TdLei1LrCwpq1wrxJ8jE8G47GZYLNiaPUKWdk8Ryzku+ZZTisoUOp6+UTZanHZz+GLxZNEhsOY1naEtqWrDKpZatEPbtueh/kdY53JjX0dRjyWqY4NOqcvVXQpBSSdbdYoSi0y9Bpmx0nAcnWHVOKlWAdyVi0KpV5LsbSuxwsP4OkKHLh5tLRUnUNsgC8QZdomj8n8mXMdY6pmEKU7NzLyUBKfy319AOcVMeKUnSK2WahdHP7j5xVrXEDEPwz2aUpDJztyd7FZ5KX5+XKO04XGhhjbWziedyJ5p9DWcPSnwcop1XimHzY+Q5xJllbNfg4vYgmvLF9DoEy82k2syBpsbC8VZKkbkWpScSzXJhUnVqDUwfE0UOptpqlQMLB+UZXKV02dusHVhGIML0mptG7c5KtPg/wCZAP8AOLcPBy2RdZsWtocRnuUAFtSrQjQAE3hABULgwAIaYcLRdG0AhXleAVEJ+2hxRNSSaKhzJSmFKC8qrGZeSNUjyTcA+fpFPLI6Dg4+qt+SIq+H9SqtKYnXWxkW3dBHIWv8/vFH3EmbVJtuQ3b1PXKzKkO6KSfErkYvxkqVFGUabsuyClKdKEaE3ur+FMPk0iLEm3ouNNBKHQD4u6Uok+cRzlVI0oY9Nv8ABLpzhS66nmlV0xO3TKPHXeLQqobSmaaWrbNmBH1ia7jRQ5OBRyWvBLTh9JSGOcKtysyhD6ggIWlwXC+hHnpGVJ0y0l2iIVQ4cVTCtRUqivKW0g3+EfVt/lV/rDJRUkOjNxZstFxpVpNvuZqnzDbmxBQT8jFOUFZoQzUhXGMa4hkoZlHrK2uCIj6J6HPOzV8XSE0xR5iv4ge799tJUzLH8rfTTmYtYYdXoz8k3K2RDnlrq1bnZ2ZJzElflaN++sDExw93Ncvoy6Y4tbmYm4AvFZ7N5PdLwhYKrVgtjS6AL+qIiyaiXMLbzMzK1KpmMP0txWpbUULNuUQRl82N5MdJnWbsfYnTivs94Sf7zO5LS5knDe5CmjksfYD5xexv40cnyo1kY89rCJSke5QClpcAAQ1gUVAAhAwti2XUqvpC2IJ+Jp52nYcqUwwkqmG5dxTYHNeU5fraEekPgrkc0uJ9FSzjN2Vqjq3nF94ptg3BCCQpJTfcKKlKNtSQRyjNzNo6zhNSSoVMI1RFbpLFKLffS0qlTaslgb22N9bafaMvdmpmgoptkd+JDrDuL59iQt3DaynMn8o6xqYrS2UZJz0hKk2xLy7ik7rFgT94fNtyJsGPrG2FLqBZmSf1IsD7QyTtovQX8cmzX2kH4twjQXtpFqcvBi8ePyaNhbSmYkkqB8QsbDqIfGRNyMXeOx9uzzij4aeEo+uxvYW6c4qchbtFDB/VoknU6SmZyrKbnqIrpuiSkZEnT0IaH6cvVN4a5Dlsx6qloaoSL7XPKGJtMVqhl+Ps4o4ZdTfIhKSABzMWse5IgyfGLIlzLl0rsLFXTp/QjUnop8ZbbFClNJTL5yLAp/mBFZmzGOjNmXQa2tWqQkAW6+GIZu4F3FGs7RslOlUTuD5wuJzGXWlwehuD94pqXzJeTCoJsnP+HXjC1BrOGHXCSclSlUnmk+B0D0UEn/uEaOJ7o5HmwqXZEzUEkaxZ8aMlnibwWICqEYFuAAVG8ACCDzgAuIOsAtFqosomZJ5pf5FIIMK3odHTII8fqYmqTkzKVahVJEyw6r4SptoCUeVl7Af1aMnJfY6XiZKqiN9TdqmEH808CqmvJIddlVguAbXv11F7RFFJu15N6alkjb+jQpttDudxlJS26vMi+9uV/OLHbexnT46+yj6MigkbIGW0NTfknUPC/CjrYZkSeqSP5QkXcifNH28TE+Rlu8zKI31MT5JbMfhw7J2ZtKVkcLatgbQRbNWMFOFDk4GSumVphxOhVoD0PKEzO42YPt+3kcSa2HH01ChyT5sczQN7+UU4vQklToyHikAgHJB9iJUINSUSTbVKdSYKscMF2gZpX7EDI3KrqvF3CtlHM9EbW5RTyEgAHNf7f7xdkxePj1YqIbMsyEJHj7lNwR5kxD+mn+JGOtfe1d1RO2h+UVZOoI0cf+vIczhvRRiajVenN/8AqVya1sp5KWnXKfUAxRupk3Ka9tDv9lXELmHpxyryyVJm8PuCafaTqp2RX4H0gc8vhV/2xfxyrZzHLgdKKZUmatT2J2WdS9LvoDiFp2Uki4MX07VnOSh1bRmA3TCjCh2gAA7QAATAAgpMABpNoB552y21JOxFrQV+ifdIaDiFiChS7MzJzUwFPpBs0ynOq/mBp84yORkgtM3eJgzTkuqIP9pHFdMcoTUq3Qm5d3vi2Jw2CzpqLD23vFbjyU5NROmfHngj7mR6YxbaA4psp0bbGby8osvZZxU0jFA71ajeySR94e9E0YWwqjqEtp/KLC33hmLzbHeorrjSRZkGlJShNt9DDskrZV4eKoGQ3KhCytPUqhFKi7hhUmmODh5aX0MrVZOgII6iJrTVMzubi6yU0S64bOrVg+VVvkBTa+45GKEnRnTXyFlSO/JOY23sIdFWrIpKjBnpFXcqN7A8okSI7t0R547slVFnZlar93awGwF7RcwNWU8yfgYWjNiaW2P4W1KJETuWzU4+P4GbU0JS4q3hsEI+QMMb1ZLGN5Ev8iKhNp2YXuDf7RUk7ikaEY/yykPHwFmGZSsSy5hSm2V3SVgflBB1ihlkozJc0HLEqNowHW/+H/E5irNgGVS8W5lpOocYUoocB8rFJ9os4patbMTkQ7Ron5wfqn7ABw0twOSAu7SnSd2dy16puLdR6GNSEl4OYzxttodpB8MTa/SiUJgABRgAtrOsAGvJVaEFoGcqDFOlXJmYWG2mxdSjCSksa7MlhB5H1iNTiXHs5iFapeWWuRkr2GQ/vHPU8vSOd5XqEpOoHUcP02K3LZo83RG3FKHdgpUSTm1v6mMOWSU3cmdVihDFGkQ57WabV2lSkuUqQo94ptAskagX+Qjc9Ocdsg53zwpIbRYbZkEgHdNySNz/AFeLfmY+KUcaRgyTSVBC1XIRY+8OyMvcaClQZa76baBAKRckjnCRfWJDzl2zKBkMNhouEjb8o6mIW7ZYhBQiysuP3bp3tfSFeqGYoqnIXsNTBbpytbKbUlXoL6w9umJlh7mKyZXDGXcbwE1nSe8yhaT1BEV77owM0Os0bFSkfGNhQISbGLONWqKuRJA1YgNqB0IF7gQ6TSIoR7PRG3tGlUngxxFvE+4kE+hvD8M0JlxPyR/wu6G3tTqG1piVy2avHinjQrVEiZmc5GhWT8kwrfxHQh/LEQ20gL10GVSvmdIgey3CNtsdrgvMtsPsocb7zokDeMjlXbaLsFcUh6qlwxpHECXK0mYps0Bl76WVZQvzI2MVePzJ4JXSf/Jn8nB2TXajS8a0zjXwtlpWbk8aqnKNJuJdaKnEsrSRoDYjU2NtDHc+lcrj+oZFiWOpP8OF9Q4mbjweTtaHv4Fdt1dJkE07iE8/OgK8FUaQFLTfktI3HmNY7LnegtQ74fo5rHy4ydT0TLodekMS0iVqlMmm52Qmmw4y+0q6VJPOONnFwfWemi+t+DMUqGAW1bwAa6DCMeNVxVxKpyoM01pRU22M6kjmrzjE9SydWoI6L0rB5mzW6PIKmlhT6/CBY5dAPKObatnV9lBVAXZqlMqlA88n90LpQ2Rv52hHGxOzeiB3aPmXMRcRHpJsJQmVKJdIG+2YiNrir24WWclSxqH2NVUGjo0D19hF6L1ZBOO1ENuVylKB+lIv6kRG3+mzgj0SovU5vvCpaU31vrDJOiGUfcy9/wALLxBWvIbpbO/UwLTEk1JMolxLZbaGhcWB6jcw/wDs7JciWKEUvsVaWtP7RdlgcqHW8pA68oJJ9bKkZ7cGT84bSCHcESIIstDSUqA9BFKEvKKfKx/NGH3E1S5t/u0HuVE2/wCmLUMij5M/LiUvsAy0xOrWTm10JOgsYTJkvwOx41EYPtZU9qRpFKAvndcJI5W2/wBYMDdkmaK6MjZRkFtxS7WGYjTof6MXJy2T8GNoVHF55whIuMqlE+0F2i3GFZhOmLIaVYa+FI+8ItCzVQ0OFwvqaqTVpSYSkK7tQJB1jO5EbX+CZyWkvJLitY/wrg/DSapNvttPLTmZl2tXHFW1AHrz2iLhelcj1LJ7eGP/AGYfL58eLbyP/oi1xA4rVXiLVkvTqizJskpYk0nwoHU9T5x7Z6L6Pg9GglGNz+2eb8/mz57e6X4ayp4bkj0jrO1vsjn2v9s0PR2eu0nV+DlTTLOKcqGG3Vfv5BStUX3W2TsfLYxg+p+m4+XBySqRbwZ3jdN6Oi+CMeUXiJh9is0OcTNyjwtpopCuaVDkR0jzfLhnhl0mjYTUtoXTtEIpp1dqaKJRZ2fcICJdlTpJ8heHKLk1FfZIleiKmGuJMrxHSufQ+38WtVnWUq1R5WjD9U4WfBmfda/TrfT+ThljpPY6lAcS9LtIFiE+I+v+0YPW/Bq3+i9Wn0MUWYdXYZG7j0hegsJfKkc0K5UH6tjep1Z/xtvTrykqJ8yAfYWjaUf40kX8TSb7GrtKD87cm41BHnvDm6VCL5ytCmmX1mXFflSPvoIrt7NyGoltI+Glwwk/vXNL9EjnC+Sm7iqQlKNwUo8LYJuo87c4lfkbgipdu30YCpwPzqXBohAASPLrE6jUKK2XI8vISXhGxUlhx1EnP6Bb0wptJP0+sRyrq0V5JyzOjoHwcqrc9IS6LBCJlkKCL/lWNFD53EYylUi3zMVJS/BxHKI0+PGgH23ETWZD0zCfobLKVZdPICEuyTwyIPbEcDtQp7QNkoCSAeepEWcLpjmu8LI6S7FpZ1Q8ISAfb+jFqT2XeFGrCS4rvn1C3hQEj1MOsmSqUpGLN3Ib1JKnDp5DSFRFm0or9FVNafoCCuWyh1aTqoXt7RNxsEORkSmZvqHIngg+nkwKdWZqaqbonJlyZLmqFuqJ9vKPUPTIw401hWkeYc2U8ycpO2LAslYI1MdVSlL/AAYquKLgXpY6jkYa4uG4+B/ZZP7FxhelwYmxyUvJXnBrwPZ2aeOE1wnxqwX3lqoU4oNTzF7jLycA/iTv6XEc96twVmxuSW0X+LlUXTZ0yl5hublm32XA4y4kLQtJuFAi4MeavTo2GRg7Y3FFGC8BChyz5bqlZBSMh1QyLZj73t842PTOP7+RSfhDck+kbRz2YrE9RptM3JTDko8DdLjKrR3eXj48kemWKaMfFmyY/lB0x5OHXa2rOFVoZrckirywNy6g5HbfYxyHJ/8AFsGeTngfV/8A4b+L1zLBKObY7tc7WGD8RYOqPw007KT3w68ktMtlKirLoARodY5Hmehcrh3Ka0jo+D6nhzyW9ka35NhrAJnlKSpwHvEqB6nUfX6Rkx7Rn1Z1alCdtDY0+a7idRmV4FHf7RYkk0Ng1CSNvmnEpprqB4ipaNRzHWKEV8zoHXXQgPzA78pQoixtrFhrRTfybotzTVpc5RZGtwIapfIve11wtiApYRbbWyR7xcSMO444Ob+xy6ZTZioU1mTlG/DILDri+iiMqB87n2im35skUf5V/glN2cMQrmaszJjQPJDzd+ih4h7ED5xj5PjOjV5cVLj9iUqhZOUjOLW0idM5avAl1FkIbWQqyibAqP5RCPRInbIR9r5+XNekUh5ClEJBAUCdCbkj3i5hhPzRMnDr1sYaRQl9may65UBP1iWaaZa41W6+iw8z3ecZTdTgHyh6Zb61GUv8mNMN/wB7l2+n/k/eJE9NlHNrLGIFeuh5A/SAmLPFl1mmZnOXe0YiwUuNu5iEggXEem4I91HKea8n4ScRfl3ipFzqBHV4/BhS8mWCCLHmIsr8Ino8lPdDw6ecVpQp2iWM7VMyZZ+ykkHURM/nEi/rK0dMuyPj1WN+D0ih5zPN0tZknCTqUgAoP/5IHtHlPqmBYOS1HwzocMnOCbP/2Q=="
encoded_photo_extension = "jpeg"