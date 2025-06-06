# XAU/USD Cronjob - Gold Price Tracker

Bu proje, **Twelve Data API** üzerinden **XAU/USD (Altın/Dolar)** fiyatlarını belirli aralıklarla çekip bir **Supabase veritabanına** kaydetmek için oluşturulmuş bir Node.js cronjob uygulamasıdır.

## Özellikler

- Twelve Data'dan gerçek zamanlı XAU/USD verisi çeker.
- Veriyi Supabase'e tarih ve saat bilgisiyle kaydeder.
- CRON tabanlı otomatik çalıştırma desteği vardır.
- `.env` ile yapılandırılabilir.

## Kurulum

### Gereksinimler

- Node.js
- Supabase hesabı
- Twelve Data API Key

### Adımlar

1. Reponun kopyasını alın:
   ```bash
   git clone https://github.com/electrichunter/xausd-cron.git
   cd xausd-cron
