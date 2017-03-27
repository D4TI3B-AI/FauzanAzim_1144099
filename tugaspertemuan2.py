graph = {'garden permata': ['sari rasa', 'setraria'],
             'sari rasa': ['sarijadi'],
             'sarijadi': ['gegerkalong'],
             'gegerkalong': ['setiabudhi'],
             'setiabudhi': ['rumah mode'],
             'setraria': ['prof dr sutami'],
             'prof dr sutami': ['setiabudhi'],
             
        }
def mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[]):
        jalur = jalur + [jalanawal]
        if jalanawal == jalantujuan:
            return jalur
        if not graph.has_key(jalanawal):
            return None
        jalurpendek = None
        for node in graph[jalanawal]:
            if node not in jalur:
                newjalur = mencari_jalur_terpendek(graph, node, jalantujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Jalan dari garden permata hotel bandung ke Rumah Mode factory Outlet")
print("(garden permata,sari rasa,sarihadi,gegerkalong,setiabudhi,rumah mode")
print("(setraria,prof dr sutami)")
print("\n")
jalanawal = raw_input("Masukan jalanawal : ")
jalantujuan = raw_input("Masukan jalantujuan : ")
hasil = mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[])
print "Jalur Terpendek", hasil
