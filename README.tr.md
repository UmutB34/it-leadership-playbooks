# IT Yönetimi Playbook'ları (Türkçe özet)

Bu depo, yirmi yıllık kurumsal BT operasyonu deneyiminden çıkardığım çalışma notlarını ve şablonları içeriyor. Ana içerik İngilizce; burada ne bulacağınızı kısaca anlatıyorum.

Hiçbir kurum, tedarikçi, sistem, tutar veya kişi adı yok. Notlar genel yöntemi anlatıyor, kimsenin iç yapısını değil.

## İçinde ne var

- **Yöntem notları (`case-studies/`):** Felaket kurtarma testi, BT karnesi (KPI), ofis ağı yenileme, denetime yanıt verme, yönetilen hizmet maliyetini inceleme, farkındalık programı, loglama ve misafir Wi-Fi tasarımı, birden fazla lokasyonu kıyaslama.
- **Playbook'lar (`playbooks/`):** BT bütçe modeli, servis masası ve ITSM, günlük operasyon kontrol listesi, uç nokta operasyonu, yama yönetimi, zafiyet yönetimi, sıkılaştırma, denetime hazırlık, KPI kataloğu, tedarikçi yönetimi, proje iş planı, çok lokasyonlu standardizasyon ve planlı kapatma-açma.
- **Geçiş playbook'ları:** İş birimlerinin kesinti toleransına göre geçiş planlama, dosya sunucusu ve DFS geçişi, dosya erişim yetkilerinin sahip tarafından gözden geçirilmesi, e-posta ve ortak çalışma geçişi, santral geçişi, 20 tür geçiş projesi için katalog, ITIL/COBIT/PMBOK/CISSP ile eşleme, otomasyon ve yapay zekâ ile çalışma, halka açık şirketlerde kapalı ortam yapay zekâ ve veri güvenliği.
- **Şablonlar (`templates/`):** Bütçe tablosu, KPI tablosu, değişiklik talebi, tedarikçi inceleme listesi, tolerans matrisi, geçiş çalışma kitabı (runbook), kullanıcı duyurusu, eski-yeni eşdeğerlik listesi.
- **Akademik çalışmalar (`academic/`):** Yüksek lisans ders projeleri.

## Nasıl kullanılır

Her belge kısa tutuldu: amaç, yöntem, nasıl ölçülür, neyi yanlış yapmamalı. Kendi ortamınıza göre uyarlamak için kopyalayıp düzenleyin. Şablonlar sade CSV ve Markdown dosyaları, herhangi bir tablo programıyla açılır.

## Temel yaklaşım

- Geçişler, hizmeti kullanan iş birimlerinin dayanabileceği kesintiye göre planlanır.
- Erişim yetkilerini BT değil, verinin sahibi onaylar.
- Bir işi bitti saymak için kanıt gerekir.
- Geri dönüş yolu, işe başlamadan önce yazılır.

## İletişim

Umut Becan — BT altyapı, güvenlik ve hizmet operasyonları. LinkedIn profilimden ulaşabilirsiniz.

## Lisans
Belgeler: [CC BY 4.0](LICENSE). **Kaynak göstermek zorunludur**, ifade için [ATTRIBUTION.md](ATTRIBUTION.md) dosyasına bakın.
Yazılım (`scripts/`, `tests/`, `academic/computer-service-records/`): [MIT](LICENSE-CODE).
