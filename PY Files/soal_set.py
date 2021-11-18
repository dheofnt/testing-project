setMovieKesukaanku = set(input('Masukkan 5 Film kesukaan anda dipisahkan dengan koma : ').split(','))
setMovieKesuakaanTemanKu = set(input('Masukkan 5 Film Kesukaan teman anda dipisahkan dengan koma : ').split(','))

setMoviaKesamaan = setMovieKesukaanku.intersection(setMovieKesuakaanTemanKu)
print('Persentase moive kesukaanku dan temanku adalah {}%'.format((len(setMoviaKesamaan) / len(setMovieKesukaanku)) * 100))

