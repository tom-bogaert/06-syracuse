"""Programme principal pour la suite de Syracuse"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Trace la suite de Syracuse"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    # votre code ici
    l = [n]

    while n != 1:
        if n%2 == 0:
            n = n//2
        else :
            n = n*3+1
        l.append(n)

    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    # votre code ici
    return len(l)-1

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici

    n = 0
    for i in l[1:]:
        if i < l[0]:
            break
        n += 1
    return n


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    return max(l)


#### Fonction principale


def main():
    """fonction principale"""
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(3)
    #syr_plot(lsyr)
    print(lsyr)
    print(f"temps_de_vol {temps_de_vol(lsyr)}")
    print(f"temps_de_vol_en_altitude {temps_de_vol_en_altitude(lsyr)}")
    print(f"altitude_maximale {altitude_maximale(lsyr)}")


if __name__ == "__main__":
    main()
