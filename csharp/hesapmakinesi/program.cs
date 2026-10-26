// 1. Kullanıcıdan birinci sayıyı al
Console.Write("Birinci sayıyı giriniz: ");
double sayi1 = Convert.ToDouble(Console.ReadLine());

// 2. Kullanıcıdan ikinci sayıyı al
Console.Write("İkinci sayıyı giriniz: ");
double sayi2 = Convert.ToDouble(Console.ReadLine());

// 3. İşlem menüsünü ekrana yazdır
Console.WriteLine("----- HESAP MAKİNESİ -----");
Console.WriteLine("1 - Toplama");
Console.WriteLine("2 - Çıkarma");
Console.WriteLine("3 - Çarpma");
Console.WriteLine("4 - Bölme");

// 4. Kullanıcıdan işlem seçmesini iste
Console.Write("İşlem seçiniz (1-4): ");
int islem = Convert.ToInt32(Console.ReadLine());

// 5. Seçilen işlemi yap
if (islem == 1)
{
    double sonuc = sayi1 + sayi2;
    Console.WriteLine("Sonuç: " + sonuc);
}
else if (islem == 2)
{
    double sonuc = sayi1 - sayi2;
    Console.WriteLine("Sonuç: " + sonuc);
}
else if (islem == 3)
{
    double sonuc = sayi1 * sayi2;
    Console.WriteLine("Sonuç: " + sonuc);
}
else if (islem == 4)
{
    if (sayi2 != 0)
    {
        double sonuc = sayi1 / sayi2;
        Console.WriteLine("Sonuç: " + sonuc);
    }
    else
    {
        Console.WriteLine("Hata! Sıfıra bölme yapılamaz.");
    }
}
else
{
    Console.WriteLine("Hatalı işlem seçtiniz!");
}

Console.WriteLine("Program sona erdi.");
