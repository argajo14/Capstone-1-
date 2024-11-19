listPasien=[
        {
            'nama':'Arga Jonathan',
            'ruangan':'Anggrek',
            'no registrasi':'1001410991003',
            'tanggal masuk':'10 Oktober 2024'
        },
        {   
            'nama':'Sifra Siregar',
            'ruangan':'Rembulan',
            'no registrasi':'1001410991004',
            'tanggal masuk':'11 Oktober 2024'
              
        },
        {
            'nama':'Ruben Binsar',
            'ruangan':'Rembulan',
            'no registrasi':'1001410991006',
            'tanggal masuk':'13 Oktober 2024'
        },
        {
            'nama':'Helena Jovana',
            'ruangan':'Mawar',
            'no registrasi':'1001410991005',
            'tanggal masuk':'14 Oktober 2024'
        },
        {
            'nama':'Yosephine',
            'ruangan':'Mawar',
            'no registrasi':'1001410991002',
            'tanggal masuk':'14 Oktober 2024'
        },
        {
            'nama':'Momo Pug',
            'ruangan':'Mawar',
            'no registrasi':'1001410991023',
            'tanggal masuk':'15 Oktober 2024'
        },
        {
            'nama':'Domina French',
            'ruangan':'Mawar',
            'no registrasi':'1001410991053',
            'tanggal masuk':'15 Oktober 2024'
        }
    ]
    
  

def menampilkanDaftarPasien():
    print("Daftar Nama Pasien Rumah Sakit Harapan Ayah \n")
    print("{:<5} {:<20} {:<15} {:<20} {:<15}".format("No", "Nama", "Ruangan", "No Registrasi", "Tanggal Masuk"))
    print("="*80)
    for i in range(len(listPasien)):
        print("{:<5} {:<20} {:<15} {:<20} {:<15}".format(
            i+1,
            listPasien[i]['nama'],
            listPasien[i]['ruangan'],
            listPasien[i]['no registrasi'],
            listPasien[i]['tanggal masuk']
            ))

def menambahkanPasien():
    while(True):
        namaPasien  = input('Nama Pasien : ')
        namaRuangan = input('Ruangan : ')
        nomorRegistrasi = input('No Registrasi(13 digit) : ')
        if len(nomorRegistrasi) != 13 or not nomorRegistrasi.isdigit():
            print("Masukan nomor registrasi yang valid, berupa 13 digit angka.")
            continue
        tanggalMasuk = input("Tanggal Masuk : ")
        while(True):
            warningPenambahan = input(f'''
            Apakah Anda yakin untuk menambahkan:
            Nama Pasien: {namaPasien}
            Ruangan: {namaRuangan}
            No Registrasi: {nomorRegistrasi}
            Tanggal Masuk: {tanggalMasuk}
            ke dalam database? (ya/tidak): ''')
            if warningPenambahan.lower() == 'ya':
                listPasien.append({
                'nama': namaPasien,
                'ruangan': namaRuangan,
                'no registrasi':nomorRegistrasi,
                'tanggal masuk':tanggalMasuk
                    })
                print(f"Pasien {namaPasien} telah ditambahkan ke daftar pasien Rumah Sakit Harapan Ayah")
                break
            elif warningPenambahan == 'tidak':
                print('Mengulangi input data pasien')
                break
            else:
                print("Input tidak valid. Harap pilih 'ya' atau 'tidak'.")
                continue
        menampilkanDaftarPasien()    
        break
        
def menghapusPasien():

    if len(listPasien)== 0:
        print("Daftar pasien kosong. Tidak ada pasien yang dapat dihapus.")
        return
        
    while True:
        menampilkanDaftarPasien()
        noInputPasien = input('Masukkan no urut siswa yang ingin dihapus :\n\n\n(atau ketik kembali untuk ke menu utama.)')

        if noInputPasien.lower() == 'kembali':
            print('Penghapusan Pasien dibatalkan')
            return

        if noInputPasien.isdigit():
            noUrutPasien = int(noInputPasien)
            if noUrutPasien  < 1:
                print('Nomor input tidak valid')
            elif noUrutPasien > len(listPasien):
                print(f'Nomor input tidak valid, Masukkan nomor antara no 1 hingga {len(listPasien)}')
            else:
                namaPasien = listPasien[noUrutPasien - 1]['nama']
                konfirmasi = input(f'Apakah anda yakin akan menghapus {namaPasien}? (ya/tidak)')
                if konfirmasi == 'ya':
                   del listPasien[noUrutPasien-1]
                   print(f'Pasien atas nama {namaPasien} berhasil dihapus.')
                   menampilkanDaftarPasien()
                elif konfirmasi == 'tidak':
                    print("Penghapusan dibatalkan")
                break
        else:
            ('Input tidak valid. Harap masukkan nomor urut pasien.')
    
def mengubahPasien():
    menampilkanDaftarPasien()
    while True:
        noUrut = input('Masukan nomor pasien yang ingin diubah:(ketik "kembali" untuk kembali ke menu utama): ')

        if noUrut.isdigit():
            noUrut = int(noUrut)

            valid_urut =list(range(1,len(listPasien)+1))

            if noUrut in valid_urut :
                pasien = listPasien[noUrut - 1]
                pasien['nama'] = input(f'Nama baru ({pasien["nama"]}): ') or pasien['nama']
                pasien['ruangan'] = input(f'Ruangan baru ({pasien["ruangan"]}): ') or pasien['ruangan']
                pasien['no registrasi'] = input(f'No Registrasi baru ({pasien["no registrasi"]}): ') or pasien['no registrasi']
                pasien['tanggal masuk'] = input(f'Tanggal Masuk baru ({pasien["tanggal masuk"]}): ') or pasien['tanggal masuk']
                print(f'Pasien {pasien["nama"]} telah diperbarui.')
                break
            else:
                 print(f"Nomor urut tidak valid. Masukkan nomor urut antara 1 dan {len(listPasien)}.")
        elif noUrut == 'kembali':
            print("Kembali ke menu utama.")
            break
        else:
            print("Input tidak valid. harap masukkan angka")

def mencariPasien():
    while(True):
        pilihanPencarian=input("Pilihan pencarian (nama/ruangan/nomor/kembali): ").lower()
        if pilihanPencarian == 'nama':
            cariNama=input("Masukan nama pasien : ")
            hasil= [pasien for pasien in listPasien if pasien['nama'].lower() == cariNama.lower()]
            if hasil:
                for pasien in hasil:
                    print(f"Nama: {pasien['nama']}, Ruangan: {pasien['ruangan']}, No Registrasi: {pasien['no registrasi']}, Tanggal Masuk: {pasien['tanggal masuk']}")
            else:
                print(f'Pasien dengan nama "{cariNama}" tidak ditemukan')
        elif pilihanPencarian == 'ruangan':
            cariRuangan = input("Masukkan nama ruangan: ")
            hasil = [pasien for pasien in listPasien if pasien['ruangan'].lower() == cariRuangan.lower()]
            if hasil:
                for pasien in hasil:
                    print(f"Nama: {pasien['nama']}, Ruangan: {pasien['ruangan']}, No Registrasi: {pasien['no registrasi']}, Tanggal Masuk: {pasien['tanggal masuk']}")
                else:
                    print(f"Pasien di ruangan '{cariRuangan}' tidak ditemukan.")
        elif pilihanPencarian == 'nomor':
            cariNoRegistrasi = input("Masukkan nomor registrasi: ")
            if len(cariNoRegistrasi) != 13 or not cariNoRegistrasi.isdigit():
                print("Masukan nomor registrasi yang valid, berupa 13 digit angka.")
                continue
            hasil = [pasien for pasien in listPasien if pasien['no registrasi'] == cariNoRegistrasi]
            if hasil:
                for pasien in hasil:
                    print(f"Nama: {pasien['nama']}, Ruangan: {pasien['ruangan']}, No Registrasi: {pasien['no registrasi']}, Tanggal Masuk: {pasien['tanggal masuk']}")
            else:
                print(f"Pasien dengan nomor registrasi '{cariNoRegistrasi}' tidak ditemukan.")
        elif pilihanPencarian == 'kembali':
            print("Kembali ke menu utama.")
            break

        else:
            print("Pilihan pencarian tidak valid. Harap pilih 'nama', 'ruangan', atau 'nomor'.")

        break
while True :
    pilihanMenu = input('''
        Selamat Datang di Data Pasien Rumah Sakit Harapan Ayah
        
        List Menu(pilih salah satu) :
        1. Daftar Pasien
        2. Tambah Pasien
        3. Hapus Pasien
        4. Ubah Pasien
        5. Cari Pasien                
        7. Exit Program
        
        Masukkan angka Menu yang ingin dijalankan : ''')

    if pilihanMenu == '1':
        menampilkanDaftarPasien()
    elif pilihanMenu == '2':
        menambahkanPasien()
    elif pilihanMenu == '3':
        menghapusPasien()   
    elif pilihanMenu == '4':
        mengubahPasien()
    elif pilihanMenu == '5':
        mencariPasien()
    elif pilihanMenu == '7':
            print("Terima kasih telah menggunakan aplikasi informasi data pasien Rumah Sakit Harapan Ayah")
            break