HELP_1 = """<b><u>Admin KOMUTLARI :</b></u>

Komutları, kanal için kullanmak amacıyla komutların başına <b>c</b> ekleyin.

<code>/duraklat</code> : Mevcut oynatılan yayını duraklatır.
<code>/devam</code> : Duraklatılan yayını yeniden başlatır.
<code>/atla</code> : Mevcut oynatılan yayını atlar ve sıradaki şarkıyı çalmaya başlar.
<code>/dur</code> veya <code>/stop</code> : Kuyruğu temizler ve mevcut yayını sonlandırır.
<code>/player</code> : Etkileşimli bir oynatıcı paneli alırsınız.
<code>/queue</code> : Kuyruğa alınan şarkıların listesini gösterir.
"""

HELP_2 = """
<b><u>YETKİLİ KULLANICILAR :</b></u>

Yetkili kullanıcılar, sohbetin içinde yönetici haklarına sahip olmadan botta yönetici haklarına sahip olabilirler.

<code>/auth</code> [kullanıcı_adı/kullanıcı_id] : Bir kullanıcıyı botun yetkili kullanıcılar listesine ekler.
<code>/unauth</code> [kullanıcı_adı/kullanıcı_id] : Bir yetkili kullanıcıyı yetkili kullanıcılar listesinden kaldırır.
<code>/authusers</code> : Grubun yetkili kullanıcılar listesini gösterir.
"""

HELP_3 = """
<u><b>YAYIN ÖZELLİĞİ</b></u> [YALNIZCA SÜDÖRLER İÇİN] :

<code>/broadcast</code> [mesaj veya bir mesaja yanıt ver] : Botun servis sohbetlerine bir mesaj yayınlar.

<u>Yayın Modları :</u>
<b><code>-pin</code></b> : Yayınladığınız mesajı servis sohbetlerinde sabitler.
<b><code>-pinloud</code></b> : Yayınladığınız mesajı servis sohbetlerinde sabitler ve üyelerine bildirim gönderir.
<b><code>-user</code></b> : Mesajı, botu başlatan kullanıcılara gönderir.
<b><code>-assistant</code></b> : Mesajı botun asistan hesabından yayınlar.
<b><code>-nobot</code></b> : Botu, mesajı yayınlamamak için zorlar.

<b>ÖRNEK:</b> <code>/broadcast -user -assistant -pin test broadcast</code>
"""

HELP_4 = """<u><b>SOHBET KARANLIK LİSTE ÖZELLİĞİ :</b></u> [YALNIZCA SÜDÖRLER İÇİN]

Botumuzu kullanmak isteyen sohbetleri kısıtlamak için.

<code>/blacklistchat</code> [sohbet ID] : Bir sohbeti botu kullanmaktan engeller.
<code>/whitelistchat</code> [sohbet ID] : Kara listeden bir sohbeti çıkarır.
<code>/blacklistedchat</code> : Kara listeye alınan sohbetlerin listesini gösterir.
"""

HELP_5 = """
<u><b>KULLANICIYI ENGELLEME:</b></u> [YALNIZCA SÜDÖRLER İÇİN]

Kara listeye alınan kullanıcıyı engellemeye başlar, böylece bot komutlarını kullanamaz.

<code>/block</code> [kullanıcı adı veya bir kullanıcıya yanıt ver] : Kullanıcıyı botumuzdan engeller.
<code>/unblock</code> [kullanıcı adı veya bir kullanıcıya yanıt ver] : Engellenmiş kullanıcıyı engelden çıkarır.
<code>/blockedusers</code> : Engellenmiş kullanıcıların listesini gösterir.
"""

HELP_6 = """
<u><b>KANALDA OYNATMA KOMUTLARI:</b></u>

Kanalda ses/video yayını yapabilirsiniz.

<code>/coynat</code> : İstenilen ses parçasını kanalın video sohbetinde yayına başlatır.
<code>/cvplay</code> : İstenilen video parçasını kanalın video sohbetinde yayına başlatır.
<code>/cplayforce</code> veya <code>/cvplayforce</code> : Devam eden yayını durdurur ve istenilen parçayı yayına başlatır.

<code>/channelplay</code> [sohbet kullanıcı adı veya ID] veya [DEVRE DIŞI] : Kanalı bir gruba bağlar ve grup içinde gönderilen komutlarla parçaların yayına başlamasını sağlar.
"""

HELP_7 = """
<u><b>GLOBAL YASAKLAMA ÖZELLİĞİ</b></u> [SADECE SÜDÖERLER İÇİN]:

<code>/gban</code> [KULLANICI ADI veya BİR MESAJI CEVAPLA] : Kullanıcıyı tüm sunucu sohbetlerinden global olarak yasaklar ve botu kullanmalarını engeller.
<code>/ungban</code> [KULLANICI ADI veya BİR MESAJI CEVAPLA] : Global olarak yasaklanmış kullanıcıyı global yasaklamadan kaldırır.
<code>/gbannedusers</code> : Global olarak yasaklanmış kullanıcıların listesini gösterir.
"""

HELP_8 = """
<b><u>LOOP AKIŞI:</b></u>

<b>DEVAM EDEN AKIŞI LOOP MODUNA ALIR</b>

<code>/dongü</code> [enable/disable] : DEVAM EDEN AKIŞ İÇİN LOOP MODUNU AÇAR/KAPATIR
<code>/dongü</code> [1, 2, 3, ...] : VERİLEN DEĞER İÇİN LOOP MODUNU AÇAR
"""

HELP_9 = """
<u><b>BAKIM MODU</b></u> [YALNIZCA SÜDÖRLER İÇİN]:

<code>/logs</code> : BOT'UN LOGLARINI GETİRİR.
<code>/logger</code> [enable/disable] : BOT, ÜZERİNDE YAPILAN AKTİVİTELERİ LOGLAMAYA BAŞLAR/KAPATIR.
<code>/maintenance</code> [enable/disable] : BOT'UN BAKIM MODUNU AÇAR/KAPATIR.
"""

HELP_10 = """
<b><u>PING & İSTATİKLER:</b></u>

<code>/start</code> : MÜZİK BOTUNU BAŞLATIR.
<code>/help</code> : KOMUTLARIN AÇIKLAMALARIYLA BİR YARDIM MENÜSÜ GÖSTERİR.
<code>/ping</code> : BOT'UN PİNGİNİ VE SİSTEM İSTATİKLERİNİ GÖSTERİR.
<code>/stats</code> : BOT'UN GENEL İSTATİKLERİNİ GÖSTERİR.
"""

HELP_11 = """
<u><b>PLAY KOMUTLARI:</b></u>

<b>v:</b> VİDEO OYNATMAK İÇİN KULLANILIR.
<b>force:</b> ZORLA OYNATMAK İÇİN KULLANILIR.

<code>/play</code> veya <code>/voynat</code> : İSTENEN MÜZİK PARÇASINI VİDEOCHAT'TE OYNATIR.
<code>/playforce</code> veya <code>/vplayforce</code> : DEVAM EDEN AKIŞI DURDURUR VE İSTENEN MÜZİK PARÇASINI ZORLA OYNATIR.
"""

HELP_12 = """
<b><u>ŞUFLÖ İÇİN KUYRUK KOMUTLARI:</b></u>

<code>/shuffle</code> : KUYRUĞU KARIŞTIRIR.
<code>/queue</code> : KARIŞTIRILMIŞ KUYRUĞU GÖSTERİR.
"""

HELP_13 = """
<b><u>AKIŞTA ARAMA KOMUTLARI:</b></u>

<code>/seek</code> [SÜRE saniye cinsinden] : AKIŞI VERİLEN SÜREYE GÖRE ARAR.
<code>/seekback</code> [SÜRE saniye cinsinden] : AKIŞI GERİYE, VERİLEN SÜREYE GÖRE ARAR.
"""

HELP_14 = """
<b><u>ŞARKI İNDİRME</b></u>

<code>/song</code> [ŞARKI ADI/YouTube URL] : YouTube'dan herhangi bir parçayı mp3 veya mp4 formatında indirir.
"""

HELP_15 = """
<b><u>HIZ KOMUTLARI :</b></u>

Şu anki yayının oynatma hızını kontrol edebilirsiniz. [Yalnızca yöneticiler]

<code>/speed</code> veya <code>/playback</code> : Grup içinde ses oynatma hızını ayarlamak için.
<code>/cspeed</code> veya <code>/cplayback</code> : Kanal içinde ses oynatma hızını ayarlamak için.
"""

HELP_16 = """
<b><u>TOPLU İŞLEM KOMUTLARI :</b></u>

NOT: Toplu işlemleri yalnızca grup sahibi kullanabilir.
<code>/gstat</code> : Grup istatistiklerini getirir.
<code>/leaveall</code> : (Sahip tarafından çalıştırılır)
<code>/banall</code> : Tüm grup üyelerini yasaklar. (Sadece grup sahibi çalıştırabilir)
<code>/unbanall</code> : Tüm yasaklı grup üyelerini serbest bırakır. (Sadece grup sahibi çalıştırabilir)
<code>/muteall</code> : Tüm grup üyelerini sessize alır. (Sadece grup sahibi çalıştırabilir)
<code>/unmuteall</code> : Tüm sessize alınmış grup üyelerinin sessizliğini açar. (Sadece grup sahibi çalıştırabilir)
<code>/kickall</code> : Tüm grup üyelerini atar. (Sadece grup sahibi çalıştırabilir)
<code>/unpinall</code> : Grubun tüm sabitlenmiş mesajlarını sabitlikten çıkarır. (Sadece grup sahibi çalıştırabilir)
<code>/deleteall</code> : Grubun tüm mesajlarını siler, bazı izinler gerektirir:
Yönetici hakları olan bot için:
1. <code>Mesajları silme bot</code>
2. <code>Üye yükseltme bot</code>
3. <code>Üye davet etme bot</code>

NOT: (Toplu işlem yalnızca grup sahibi tarafından kullanılabilir)
"""
HELP_17 = """
<b><u>YAYIN LİSANS İÇİN ÖZELLİKLER:</b></u>

NOT: Artık aylık ve haftalık yayın abone üyeliklerini bizden satın alabilirsiniz. Haftalık üyelik için 4 yayın, aylık üyelik için ise 14 yayın veriyoruz ve yayın göndermeye iki gün sonra başlayabilirsiniz.

<code>/gcast</code> : Abone kullanıcıları.
<code>/gcast -user hii</code>

<code>/addpro</code> : Kullanıcıya/ID'ye/kullanıcı adına gün eklemek için cevap verin. (Sahip)
<code>/addpro @AMBOTYT 7</code>

<code>/rmpro</code> : Kullanıcıdan/ID'den/kullanıcı adından gün kaldırmak için cevap verin. (Sahip)
<code>/rmpro @AMBOTYT</code>

<code>/prolists</code> : Tüm abone kullanıcıların listesini alır.
"""
