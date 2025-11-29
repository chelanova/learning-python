import requests

BASE_URL = "https://restcountries.com/v3.1"
def get_country_by_name(country_name):
    url = f"{BASE_URL}/name/{country_name}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Negara {country_name} tidak ditemukan")
            return None
        else:
            print(f"Error: {response.status_code}")
            return None
        
    except requests.exceptions.ConnectionError:
        print("Tidak bisa terhubung ke internet!")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def get_countries_by_region(region):
    url = f"{BASE_URL}/region/{region}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def display_country_info(country_data):
    if country_data is None:
        return
    country = country_data[0]
    
    name = country['name']['common']
    official_name = country['name']['official']
    capital = country.get('capital', ['N/A'])[0]
    region = country.get('region', 'N/A')
    subregion = country.get('subregion', 'N/A')
    population = country.get('population', 0)
    area = country.get('area', 0)
    
    
    
    languages = country.get('languages', {})
    language_list = ', '.join(languages.values()) if languages else 'N/A'
    
    currencies = country.get('currencies', {})
    currency_list = ', '.join([f"{curr['name']} ({curr['symbol']})"
                               for curr in currencies.values()]) if currencies else 'N/A'
    
    timezones = ', '.join(country.get('timezones',['N/A']))
    
    flag = country.get('flag', '🏳️')
    
    print("\n" + "="*60)
    print(f"{flag} {name.upper()}")
    print("="*60)
    print(f"Nama Resmi: {official_name}")
    print(f"Ibukota: {capital}")
    print(f"Region: {region} ({subregion})")
    print(f"Populasi: {population} jiwa")
    print(f"Luas Area: {area:,} km²")
    print(f"Bahasa: {language_list}")
    print(f"Mata Uang: {currency_list}")
    print(f"Timezone: {timezones}")
    print("\n" + "="*60)
    
def display_region_summary(countries_data):
    if countries_data is None or len(countries_data) == 0:
        return
    print("\n" + "="*60)
    print(f"Ditemukan {len(countries_data)} Negara:")
    print("="*60)
    
    for country in countries_data:
        name = country['name']['common']
        capital = country.get('capital', ['N/A'])[0]
        population = country.get('population', 0)
        flag = country.get('flag', '🏳️')
        
        print(f"{flag} {name:<30} | Ibukota: {capital:<20} | Populasi: {population:>12,}")
    print("="*60)
    
def main():
    print("🌍 COUNTRY INFO APP - REST Countries API")
    print("="*60)
    
    while True:
        print("\nPilih menu:")
        print("1. Cari negara berdasarkan nama")
        print("2. Lihat negara berdasarkan region")
        print("3. Exit")
        
        choice = input("\nPilihan (1/2/3): ").strip()
        
        if choice == '1':
            country_name = input("\n Masukkan nama Negara: ").strip()
            if country_name:
                country_data = get_country_by_name(country_name)
                display_country_info(country_data)
            else:
                print("Nama Negara tidak boleh kosong!")
                
        elif choice == '2':
            print("\nPilih region:")
            print("- Asia")
            print("- Europe")
            print("- Africa")
            print("- Americas")
            print("- Oceania")
            region = input("\n Masukkan Wilayah: ").strip()
            if region:
                countries_data = get_countries_by_region(region)
                display_region_summary(countries_data)
            else:
                print("Region tidak boleh kosong!")
                
                
        elif choice == '3':
            print("Terima kasih! Sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid")
        
if __name__ == "__main__":
    main()