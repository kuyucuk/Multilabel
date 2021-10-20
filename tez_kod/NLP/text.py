import xlwt
from openpyxl import Workbook,load_workbook
from xlwt import Workbook


wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

dosya_ismi = "acik1"

toplam = open(""+dosya_ismi+".txt", "r", encoding="utf-8")
icerik = toplam.read()


icerik="Sürat Kargo Müşteri Memnuniyeti Umurlarında Değil--> Korona virüs belası sebebiyle tüm aile bireyleri olarak Eve ® hapis olduğumuz bir günde gelen kargomu teslim etmeyip işin kolayına kaçarak not bırakıp giden işgüzar personellerden, buna prim veren kargo şirketinden şikayetçiyim. Sürat kelimesi jet hızıyla dağıtıma çıkıp geri dönmek anlamına geliyor onlar için. Müşteri memnuniyeti umurlarında değil."

icerik = str(icerik).replace("A", "a")
icerik = str(icerik).replace("B", "b")
icerik = str(icerik).replace("C", "c")
icerik = str(icerik).replace("Ç", "ç")
icerik = str(icerik).replace("D", "d")
icerik = str(icerik).replace("E", "e")
icerik = str(icerik).replace("F", "f")
icerik = str(icerik).replace("G", "g")
icerik = str(icerik).replace("Ğ", "ğ")
icerik = str(icerik).replace("H", "h")
icerik = str(icerik).replace("I", "ı")
icerik = str(icerik).replace("İ", "i")
icerik = str(icerik).replace("J", "j")
icerik = str(icerik).replace("K", "k")
icerik = str(icerik).replace("L", "l")
icerik = str(icerik).replace("M", "m")
icerik = str(icerik).replace("N", "n")
icerik = str(icerik).replace("O", "o")
icerik = str(icerik).replace("Ö", "ö")
icerik = str(icerik).replace("P", "p")
icerik = str(icerik).replace("R", "r")
icerik = str(icerik).replace("S", "s")
icerik = str(icerik).replace("Ş", "ş")
icerik = str(icerik).replace("T", "t")
icerik = str(icerik).replace("U", "u")
icerik = str(icerik).replace("Ü", "ü")
icerik = str(icerik).replace("V", "v")
icerik = str(icerik).replace("Y", "y")
icerik = str(icerik).replace("Z", "z")

icerik = str(icerik).replace("i̇̇", "i")
icerik = str(icerik).replace("İ", "i")
icerik = str(icerik).replace("I", "ı")
icerik = str(icerik).replace("Ö", "ö")
icerik = str(icerik).replace("Ü", "ü")
icerik = str(icerik).replace("Ç", "ç")
icerik = str(icerik).replace("Ş", "ş")

for i in range(0, 999):
	icerik = str(icerik).replace(" "+str(i)+" ", " ")

icerik = str(icerik).replace(" . ", " ")
icerik = str(icerik).replace('"', "")
icerik = str(icerik).replace(": ", "")
icerik = str(icerik).replace(";", "")
icerik = str(icerik).replace("'", "")
icerik = str(icerik).replace(" - ", " ")
icerik = str(icerik).replace("!", "")
icerik = str(icerik).replace('%', "")
icerik = str(icerik).replace("(", "")
icerik = str(icerik).replace(")", "")
icerik = str(icerik).replace("*", "")
icerik = str(icerik).replace("/", "")
icerik = str(icerik).replace('?', "")
icerik = str(icerik).replace("’", "")
icerik = str(icerik).replace("”", "")
icerik = str(icerik).replace("“", "")
icerik = str(icerik).replace('"', "")
icerik = str(icerik).replace(",", "")
icerik = str(icerik).replace(" + ", " ")
icerik = str(icerik).replace("=", "")

icerik = str(icerik).replace(" dönem", " dönem ")
icerik = str(icerik).replace("korona dönem", " Korona_dönemi ")
icerik = str(icerik).replace("corona dönem", " Corona_dönemi ")
icerik = str(icerik).replace("pandemi dönem", " Pandemi_dönemi ")
icerik = str(icerik).replace("yurtiçi kargo", " Yurtiçi_Kargo ")
icerik = str(icerik).replace("ptt kargo", " Ptt_Kargo ")
icerik = str(icerik).replace("aras kargo", " Aras_Kargo ")
icerik = str(icerik).replace("sürat kargo", " Sürat_Kargo ")
icerik = str(icerik).replace("surat kargo", " Sürat_Kargo ")
icerik = str(icerik).replace("mng kargo", " Mng_Kargo ")
icerik = str(icerik).replace("ups türkiye", " Ups_türkiye ")
icerik = str(icerik).replace("ay kargo", " ay_Kargo ")

icerik = str(icerik).replace("n11", " n11 ")
icerik = str(icerik).replace("trendyol", " trendyol ")
icerik = str(icerik).replace("mng", " mng ")
icerik = str(icerik).replace("sürat", " sürat ")
icerik = str(icerik).replace("sürat", " sürat ")
icerik = str(icerik).replace("yurtiçi", " yurtiçi ")
icerik = str(icerik).replace("aras", " aras ")
icerik = str(icerik).replace("ptt", " ptt ")
icerik = str(icerik).replace("ups", " ups ")

icerik = str(icerik).replace(" tarih ", " ")
icerik = str(icerik).replace(" kişi ", " ")
icerik = str(icerik).replace("çözüm notu verilmemiş", " ")
icerik = str(icerik).replace(" durum ", " ")
icerik = str(icerik).replace(" marka ", " ")
icerik = str(icerik).replace(" başlık ", " ")
icerik = str(icerik).replace(" link ", " ")
icerik = str(icerik).replace(" içerik ", " ")
icerik = str(icerik).replace(" görüntülenme ", " ")
icerik = str(icerik).replace(" daha ", " ")
icerik = str(icerik).replace(" kadar ", " ")
icerik = str(icerik).replace(" sonra ", " ")
icerik = str(icerik).replace(" çok ", " ")
icerik = str(icerik).replace(" var ", " ")
icerik = str(icerik).replace(" her ", " ")
icerik = str(icerik).replace(" hiçbir ", " ")
icerik = str(icerik).replace(" olan ", " ")
icerik = str(icerik).replace(" önce ", " ")
icerik = str(icerik).replace(" şekilde ", " ")
icerik = str(icerik).replace(" böyle ", " ")
icerik = str(icerik).replace(" dedi ", " ")
icerik = str(icerik).replace(" bile ", " ")
icerik = str(icerik).replace(" söyledi ", " ")
icerik = str(icerik).replace(" değil ", " ")
icerik = str(icerik).replace(" ancak ", " ")
icerik = str(icerik).replace(" şey ", " ")
icerik = str(icerik).replace(" dolayı ", " ")
icerik = str(icerik).replace(" aynı ", " ")
icerik = str(icerik).replace(" oldu ", " ")
icerik = str(icerik).replace(" aldım ", " ")
icerik = str(icerik).replace(" olduğunu ", " ")
icerik = str(icerik).replace(" istiyorum ", " ")
icerik = str(icerik).replace(" benim ", " ")
icerik = str(icerik).replace(" aradım ", " ")
icerik = str(icerik).replace(" aldığım ", " ")
icerik = str(icerik).replace("gündür", "gün")
icerik = str(icerik).replace(" gün ", " ")

icerik = str(icerik).replace(" bir ", " ")
icerik = str(icerik).replace(" ve ", " ")
icerik = str(icerik).replace(" veya ", " ")
icerik = str(icerik).replace(" bu ", " ")
icerik = str(icerik).replace(" için ", " ")
icerik = str(icerik).replace(" de ", " ")
icerik = str(icerik).replace(" da ", " ")
icerik = str(icerik).replace(" ile ", " ")
icerik = str(icerik).replace(" ne ", " ")
icerik = str(icerik).replace(" bana ", " ")
icerik = str(icerik).replace(" ama ", " ")
icerik = str(icerik).replace(" hiç ", " ")
icerik = str(icerik).replace(" rağmen ", " ")
icerik = str(icerik).replace(" olarak ", " ")
icerik = str(icerik).replace(" diye ", " ")
icerik = str(icerik).replace(" gibi ", " ")
icerik = str(icerik).replace(" hakkında", " ")
icerik = str(icerik).replace(" bu ", " ")
icerik = str(icerik).replace(" şu ", " ")
icerik = str(icerik).replace(' o ', " ")
icerik = str(icerik).replace(" ki ", " ")
icerik = str(icerik).replace("Bu", "bu")
icerik = str(icerik).replace(" beni ", " ben ")
icerik = str(icerik).replace(" ben ", " ")
icerik = str(icerik).replace(" en ", " ")
icerik = str(icerik).replace(" ya ", " ")
icerik = str(icerik).replace(" ise ", " ")
icerik = str(icerik).replace(" ın ", " ")
icerik = str(icerik).replace(" in ", " ")
icerik = str(icerik).replace(" ini ", " ")
icerik = str(icerik).replace(" ını ", " ")
icerik = str(icerik).replace("'ın", " ")
icerik = str(icerik).replace("'in", " ")
icerik = str(icerik).replace("'ini", " ")
icerik = str(icerik).replace("'ını", " ")
icerik = str(icerik).replace(" mı ", " ")
icerik = str(icerik).replace(" mi ", " ")
icerik = str(icerik).replace(" mu ", " ")
icerik = str(icerik).replace(" mü ", " ")
icerik = str(icerik).replace(" ma ", " ")
icerik = str(icerik).replace(" me ", " ")
icerik = str(icerik).replace(" ler ", " ")
icerik = str(icerik).replace(" lar ", " ")
icerik = str(icerik).replace("kaynak", " ")
icerik = str(icerik).replace(" den ", " ")
icerik = str(icerik).replace(" dan ", " ")
icerik = str(icerik).replace(" de ", " ")
icerik = str(icerik).replace(" da ", " ")
icerik = str(icerik).replace(" ım ", " ")
icerik = str(icerik).replace(" im ", " ")
icerik = str(icerik).replace(" ay ", " ")
icerik = str(icerik).replace(" ini ", " ")
icerik = str(icerik).replace(" ını ", " ")
icerik = str(icerik).replace(" olduğu ", " ")
icerik = str(icerik).replace(" geldi ", " ")
icerik = str(icerik).replace(" iş ", " ")
icerik = str(icerik).replace(" ın ", " ")
icerik = str(icerik).replace(" ıd ", " ")
icerik = str(icerik).replace(" id ", " ")

icerik = str(icerik).replace(" a ", " ")
icerik = str(icerik).replace(" b ", " ")
icerik = str(icerik).replace(" c ", " ")
icerik = str(icerik).replace(" ç ", " ")
icerik = str(icerik).replace(" d ", " ")
icerik = str(icerik).replace(' e ', " ")
icerik = str(icerik).replace(" f ", " ")
icerik = str(icerik).replace(" g ", " ")
icerik = str(icerik).replace(" ğ ", " ")
icerik = str(icerik).replace(" h ", " ")
icerik = str(icerik).replace(" ı ", " ")
icerik = str(icerik).replace(" i ", " ")
icerik = str(icerik).replace(" j ", " ")
icerik = str(icerik).replace(' k ', " ")
icerik = str(icerik).replace(" l ", " ")
icerik = str(icerik).replace(" m ", " ")
icerik = str(icerik).replace(" n ", " ")
icerik = str(icerik).replace(" o ", " ")
icerik = str(icerik).replace(" ö ", " ")
icerik = str(icerik).replace(" p ", " ")
icerik = str(icerik).replace(" r ", " ")
icerik = str(icerik).replace(' s ', " ")
icerik = str(icerik).replace(" ş ", " ")
icerik = str(icerik).replace(" t ", " ")
icerik = str(icerik).replace(" u ", " ")
icerik = str(icerik).replace(" ü ", " ")
icerik = str(icerik).replace(" v ", " ")
icerik = str(icerik).replace(" y ", " ")
icerik = str(icerik).replace(" z ", " ")
icerik = str(icerik).replace(' x ', " ")
icerik = str(icerik).replace(" w ", " ")
icerik = str(icerik).replace(" q ", " ")

if " arama" in icerik:
	if "aramak" not in icerik:
		if "aramal" not in icerik:
			if "aranmal" not in icerik:
				icerik = str(icerik).replace(" arama", " arama_yapılmaması ").replace(" aranma", " arama_yapılmaması ").replace(" aramı", " arama_yapılmaması ")
if " aranm" in icerik:
	if "aramak" not in icerik:
		if "aramal" not in icerik:
			if "aranmal" not in icerik:
				icerik = str(icerik).replace(" arama", " arama_yapılmaması ").replace(" aranma", " arama_yapılmaması ").replace(" aramı", " arama_yapılmaması ")
if "aramı" in icerik:
	if "aramak" not in icerik:
		if "aramal" not in icerik:
			if "aranmal" not in icerik:
				icerik = str(icerik).replace(" arama", " arama_yapılmaması ").replace(" aranma", " arama_yapılmaması ").replace(" aramı", " arama_yapılmaması ")


icerik = str(icerik).replace("telefon bakm", " telefonlara_bakmılmaması ")
icerik = str(icerik).replace("covid önlem", " covid_önlemi ")
icerik = str(icerik).replace("covid  önlem", " covid_önlemi ")
icerik = str (icerik).replace("\ufeff"," ")



if " olma" in icerik:
	if "olmas" not in icerik:
		if "olmal" not in icerik:
			if "olmak" not in icerik:
				icerik = str(icerik).replace(" olma ", "yok ")

icerik = str(icerik).replace("maske yok", " maske_yok ")


splitWords = icerik.split()
print(splitWords)
print(len(splitWords))

telefondegisken=0
evdedegisken=0
dagitimdegisken=0
temizdegisken=0
kapiyadegisken=0
iadedegisken=0
teslimdegisken=0
diyalogdegisken=0
kayipdegisken=0

oran=1
####################################################"Gecikti veya Dağıtıma Çıkmadı"########################################################
if 'dağıtım' in icerik:
    dagitimdegisken=dagitimdegisken+1
if 'çıkmadı' in icerik:
    dagitimdegisken=dagitimdegisken+1
if 'çıkış şube' in icerik:
    dagitimdegisken=dagitimdegisken+1
if 'gelmedi' in icerik:
    dagitimdegisken=dagitimdegisken+1
if 'beklet' in icerik:
    dagitimdegisken=dagitimdegisken+1
if 'süredir' in icerik:
    dagitimdegisken=dagitimdegisken+1
if 'gecik' in icerik:
    dagitimdegisken=dagitimdegisken+1
if 'bekli' in icerik:
    dagitimdegisken=dagitimdegisken+1
if 'hala çıkış' in icerik:
    dagitimdegisken=dagitimdegisken+1
if 'geç ' in icerik:
    dagitimdegisken=dagitimdegisken+1
if(dagitimdegisken*100)/len(splitWords)>oran:
    print("Gecikti veya Dağıtıma Çıkmadı")
    print(dagitimdegisken)
##########################################################"Evde yok notu düşüldü veya Kapıya Getirilmedi"##################################################
if 'adresiniz' in icerik:
    evdedegisken=evdedegisken+1
if 'adreste' in icerik:
    evdedegisken=evdedegisken+1
if 'evde' in icerik:
    evdedegisken=evdedegisken+1
if 'not ' in icerik:
    evdedegisken=evdedegisken+1
if 'evime' in icerik:
    evdedegisken=evdedegisken+1
if 'kapım' in icerik:
    evdedegisken=evdedegisken+1
if 'çalmıyor' in icerik:
    evdedegisken=evdedegisken+1
if 'çalmadı' in icerik:
    evdedegisken=evdedegisken+1
if 'çalmadan' in icerik:
    evdedegisken=evdedegisken+1
if 'geldik' in icerik:
    evdedegisken=evdedegisken+1
if 'yoktunuz' in icerik:
    evdedegisken=evdedegisken+1
if 'kağı' in icerik:
    evdedegisken=evdedegisken+1
if 'daire' in icerik:
    evdedegisken=evdedegisken+1
if 'bina' in icerik:
    evdedegisken=evdedegisken+1
if 'aşağı' in icerik:
    evdedegisken=evdedegisken+1
if 'inmem' in icerik:
    evdedegisken=evdedegisken+1
if 'yukarı' in icerik:
    evdedegisken=evdedegisken+1
if 'kapıya' in icerik:
    evdedegisken=evdedegisken+1
if(evdedegisken*100)/len(splitWords)>oran:
    print("Evde yok notu düşüldü veya Kapıya Getirilmedi")
    print(evdedegisken)
#################################################################"Telefonlara Cevap Verilmedi"###########################################
if 'telefonu' in icerik:
    telefondegisken=telefondegisken+1
if 'telefona' in icerik:
    telefondegisken=telefondegisken+1
if 'telefonlar' in icerik:
    telefondegisken=telefondegisken+1
if 'açmadı' in icerik:
    telefondegisken=telefondegisken+1
if 'cevap' in icerik:
    telefondegisken=telefondegisken+1
if 'açmıyor' in icerik:
    telefondegisken=telefondegisken+1
if 'ulaşılamıyor' in icerik:
    telefondegisken=telefondegisken+1
if 'ulaşamı' in icerik:
    telefondegisken=telefondegisken+1
if 'açan yok' in icerik:
    telefondegisken=telefondegisken+1
if(telefondegisken*100)/len(splitWords)>oran:
    print("Telefonlara Cevap Verilmedi")
    print(telefondegisken)
##########################################################"İade Süreci"##################################################
if 'geri gön' in icerik:
    iadedegisken=iadedegisken+1
if 'iade' in icerik:
    iadedegisken=iadedegisken+1
if 'geri yolla' in icerik:
    iadedegisken=iadedegisken+1
if(iadedegisken*100)/len(splitWords)>oran:
    print("İade Süreci")
    print(iadedegisken)
####################################################"Teslim Alınmadı veya Teslim Edilmedi"########################################################
if 'teslimat yapılm' in icerik:
    teslimdegisken=teslimdegisken+1
if 'teslimatı yapılm' in icerik:
    teslimdegisken=teslimdegisken+1
if 'teslimat yapma' in icerik:
    teslimdegisken=teslimdegisken+1
if 'teslim edilme' in icerik:
    teslimdegisken=teslimdegisken+1
if 'teslim alınma' in icerik:
    teslimdegisken=teslimdegisken+1
if 'teslim etme' in icerik:
    teslimdegisken=teslimdegisken+1
if 'teslim alma' in icerik:
    teslimdegisken=teslimdegisken+1
if(teslimdegisken*100)/len(splitWords)>oran:
    print("Teslim Alınmadı veya Teslim Edilmedi")
    print(teslimdegisken)
##########################################################"Kötü Diyalog Veya Saygısız Tutum"##################################################
if 'saygı' in icerik:
    diyalogdegisken=diyalogdegisken+1
if 'huysuz' in icerik:
    diyalogdegisken=diyalogdegisken+1
if 'laubali' in icerik:
    diyalogdegisken=diyalogdegisken+1
if 'lakayı' in icerik:
    diyalogdegisken=diyalogdegisken+1
if 'bağır' in icerik:
    diyalogdegisken=diyalogdegisken+1
if 'keyfiye' in icerik:
    diyalogdegisken=diyalogdegisken+1
if 'terbiye' in icerik:
    diyalogdegisken=diyalogdegisken+1
if ' azar' in icerik:
    diyalogdegisken=diyalogdegisken+1
if(diyalogdegisken*100)/len(splitWords)>oran:
    print("Kötü Diyalog Veya Saygısız Tutum")
    print(diyalogdegisken)
########################################################"Hasarlı veya Kayıp Paket"####################################################
if 'kayıp' in icerik:
    kayipdegisken=kayipdegisken+1
if 'kayb' in icerik:
    kayipdegisken=kayipdegisken+1
if 'hasar' in icerik:
    kayipdegisken=kayipdegisken+1
if 'parça' in icerik:
    kayipdegisken=kayipdegisken+1
if(kayipdegisken*100)/len(splitWords)>oran:
    print("Hasarlı veya Kayıp Paket")
    print(kayipdegisken)
###########################################################"Hijyen Kurallarına Uyulmadı"#################################################
if 'hijyen' in icerik:
    temizdegisken=temizdegisken+1
if 'maske' in icerik:
    temizdegisken=temizdegisken+1
if ' temiz ' in icerik:
    temizdegisken=temizdegisken+1
if 'titiz' in icerik:
    temizdegisken=temizdegisken+1
if(temizdegisken*100)/len(splitWords)>oran:
    print("Hijyen Kurallarına Uyulmadı")
    print(temizdegisken)
############################################################################################################







