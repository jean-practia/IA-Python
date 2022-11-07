from googlesearch import search 

def pesquisa():

    try: 
        query = input("Digite algo para pesquisar: ")
        for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
            print(j) 
    except ImportError:  
        print("No module named 'google' found")

    finally:
        print("Busca finalizada!")
