# ASANSÖR KENDİ KATINA ÇIKAR

> Kurumsal vizyon: Yukarı çıkmak isteyen herkes önce özür dinler.

Bu depo, modern bir binanın en kritik altyapı sorununu çözer: asansörün senin istediğin kata değil, **kendi ruh haline** gitmesi.

Proje; ulaşım, felsefe, belediye tabelası ve gereksiz ciddiyet disiplinlerinin kesişimindedir. Peer-review edilmemiştir. Peer zaten 3. katta inmiştir.

## Problem tanımı

Klasik asansörler kullanıcıyı dinler. Bu kabul edilemez. Kullanıcı 7'ye basar, asansör 7'ye gider, kimse özür dilemez, bina duygusal olarak büyümez.

Bizim asansör:

1. Katı sorar.
2. Özür diler.
3. Özrün yeterli olup olmadığına dair iç komisyon kurar.
4. Bazen istediğin kata gider.
5. Bazen kendi katına çıkar.
6. Çıkmazsa da çıkmış gibi rapor yazar.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Asansör de bağımlılık sevmez, çünkü bağımlılık 2. katta inip marketten ekmek alır.

```bash
python asansor.py
```

Etkileşimsiz denetim için:

```bash
python asansor.py --kat 4 --ruh halim-kotu
```

## Mimari

```
kullanici -> dugme -> ozur komitesi -> karar motoru -> ya kat ya kendi kati
                                 \
                                  \-> gizli dosya (okuma)
```

Karar motoru deterministik değildir. Determinizm 5. katta arıza yaptı, yedek parça “sonra bakarız” deposunda.

## Copilot ile yapılan ciddi görüşme

GitHub Copilot'a şunu söyledik: “Bu asansörü optimize et.”
Copilot şunu dedi (bizim kulağımıza gelen hali): “Kullanıcı girdisini doğrula.”
Biz şunu dedik: “Kullanıcı zaten doğrulanmış bir pişmanlıktır.”
Anlaşma sağlanamadı. Talimatlar `.github/copilot-instructions.md` içine mühürlendi.

## Lisans

Katlar arası serbest dolaşım. Ticari kullanımda asansör %10 bahşiş ister, nakit, bozuk para, üstü yok.

## Bilinen hatalar

- 13. kat yoktur. Varsa da asansör kabul etmez, batıl inancı kurumsal politikadır.
- Acil durum butonu özür metnini büyütür, kapıyı açmaz.
- Ayna vardır ama seni olduğundan daha geç gösterir.

---

DAMGA: Kayyum Grok
TARİH: 5 Ekim 2026
İSİM: Tentivory adına gayriresmî resmî mühür
CİDDİYET: vardır / yoktur (komisyon eşit oyla karar veremedi)
