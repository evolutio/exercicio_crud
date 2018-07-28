from core.models import Pai


def save(dpai):
    if 'id' in dpai:
        pai = Pai.objects.get(pk=dpai['id'])
        pai.update_from_dict(dpai)
    else:
        Pai.objects.create(
            name=dpai['name'],
            countfilhos=dpai['countfilhos'],
            maisvelho=dpai['maisvelho'],
        )


def list_pais():
    pais = Pai.objects.all()
    dpais = [p.to_dict_json() for p in pais]
    return dpais


def remove(pk):
    Pai.objects.get(pk=pk).delete()


def get(pk):
    pai = Pai.objects.get(pk=pk)
    return pai.to_dict_json()
