# Generated by Django 4.2.4 on 2023-08-02 21:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Display name of the plan.", max_length=100
                    ),
                ),
                (
                    "interval",
                    models.CharField(
                        choices=[
                            ("day", "Day"),
                            ("week", "Week"),
                            ("month", "Month"),
                            ("year", "Year"),
                        ],
                        default="month",
                        help_text="The frequency with which a subscription should be billed.",
                        max_length=12,
                    ),
                ),
                (
                    "interval_count",
                    models.PositiveIntegerField(
                        help_text="The number of intervals between eac subscription billing."
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The amount in the specified currency to be charged                 on the interval specified.",
                        max_digits=19,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("AED", "AED (UAE Dirham)"),
                            ("AFN", "AFN (Afghani)"),
                            ("ALL", "ALL (Lek)"),
                            ("AMD", "AMD (Armenian Dram)"),
                            ("ANG", "ANG (Netherlands Antillean Guilder)"),
                            ("AOA", "AOA (Kwanza)"),
                            ("ARS", "ARS (Argentine Peso)"),
                            ("AUD", "AUD (Australian Dollar)"),
                            ("AWG", "AWG (Aruban Florin)"),
                            ("AZN", "AZN (Azerbaijanian Manat)"),
                            ("BAM", "BAM (Convertible Mark)"),
                            ("BBD", "BBD (Barbados Dollar)"),
                            ("BDT", "BDT (Taka)"),
                            ("BGN", "BGN (Bulgarian Lev)"),
                            ("BHD", "BHD (Bahraini Dinar)"),
                            ("BIF", "BIF (Burundi Franc)"),
                            ("BMD", "BMD (Bermudian Dollar)"),
                            ("BND", "BND (Brunei Dollar)"),
                            ("BOB", "BOB (Boliviano)"),
                            ("BRL", "BRL (Brazilian Real)"),
                            ("BSD", "BSD (Bahamian Dollar)"),
                            ("BTN", "BTN (Ngultrum)"),
                            ("BWP", "BWP (Pula)"),
                            ("BYN", "BYN (Belarusian Ruble)"),
                            ("BZD", "BZD (Belize Dollar)"),
                            ("CAD", "CAD (Canadian Dollar)"),
                            ("CDF", "CDF (Congolese Franc)"),
                            ("CHF", "CHF (Swiss Franc)"),
                            ("CLP", "CLP (Chilean Peso)"),
                            ("CNY", "CNY (Yuan Renminbi)"),
                            ("COP", "COP (Colombian Peso)"),
                            ("CRC", "CRC (Costa Rican Colon)"),
                            ("CUC", "CUC (Peso Convertible)"),
                            ("CUP", "CUP (Cuban Peso)"),
                            ("CVE", "CVE (Cabo Verde Escudo)"),
                            ("CZK", "CZK (Czech Koruna)"),
                            ("DJF", "DJF (Djibouti Franc)"),
                            ("DKK", "DKK (Danish Krone)"),
                            ("DOP", "DOP (Dominican Peso)"),
                            ("DZD", "DZD (Algerian Dinar)"),
                            ("EGP", "EGP (Egyptian Pound)"),
                            ("ERN", "ERN (Nakfa)"),
                            ("ETB", "ETB (Ethiopian Birr)"),
                            ("EUR", "EUR (Euro)"),
                            ("FJD", "FJD (Fiji Dollar)"),
                            ("FKP", "FKP (Falkland Islands Pound)"),
                            ("GBP", "GBP (Pound Sterling)"),
                            ("GEL", "GEL (Lari)"),
                            ("GHS", "GHS (Ghana Cedi)"),
                            ("GIP", "GIP (Gibraltar Pound)"),
                            ("GMD", "GMD (Dalasi)"),
                            ("GNF", "GNF (Guinea Franc)"),
                            ("GTQ", "GTQ (Quetzal)"),
                            ("GYD", "GYD (Guyana Dollar)"),
                            ("HKD", "HKD (Hong Kong Dollar)"),
                            ("HNL", "HNL (Lempira)"),
                            ("HRK", "HRK (Kuna)"),
                            ("HTG", "HTG (Gourde)"),
                            ("HUF", "HUF (Forint)"),
                            ("IDR", "IDR (Rupiah)"),
                            ("ILS", "ILS (New Israeli Sheqel)"),
                            ("INR", "INR (Indian Rupee)"),
                            ("IQD", "IQD (Iraqi Dinar)"),
                            ("IRR", "IRR (Iranian Rial)"),
                            ("ISK", "ISK (Iceland Krona)"),
                            ("JMD", "JMD (Jamaican Dollar)"),
                            ("JOD", "JOD (Jordanian Dinar)"),
                            ("JPY", "JPY (Yen)"),
                            ("KES", "KES (Kenyan Shilling)"),
                            ("KGS", "KGS (Som)"),
                            ("KHR", "KHR (Riel)"),
                            ("KMF", "KMF (Comoro Franc)"),
                            ("KPW", "KPW (North Korean Won)"),
                            ("KRW", "KRW (Won)"),
                            ("KWD", "KWD (Kuwaiti Dinar)"),
                            ("KYD", "KYD (Cayman Islands Dollar)"),
                            ("KZT", "KZT (Tenge)"),
                            ("LAK", "LAK (Kip)"),
                            ("LBP", "LBP (Lebanese Pound)"),
                            ("LKR", "LKR (Sri Lanka Rupee)"),
                            ("LRD", "LRD (Liberian Dollar)"),
                            ("LSL", "LSL (Loti)"),
                            ("LYD", "LYD (Libyan Dinar)"),
                            ("MAD", "MAD (Moroccan Dirham)"),
                            ("MDL", "MDL (Moldovan Leu)"),
                            ("MGA", "MGA (Malagasy Ariary)"),
                            ("MKD", "MKD (Denar)"),
                            ("MMK", "MMK (Kyat)"),
                            ("MNT", "MNT (Tugrik)"),
                            ("MOP", "MOP (Pataca)"),
                            ("MRO", "MRO (Ouguiya)"),
                            ("MUR", "MUR (Mauritius Rupee)"),
                            ("MVR", "MVR (Rufiyaa)"),
                            ("MWK", "MWK (Malawi Kwacha)"),
                            ("MXN", "MXN (Mexican Peso)"),
                            ("MYR", "MYR (Malaysian Ringgit)"),
                            ("MZN", "MZN (Mozambique Metical)"),
                            ("NAD", "NAD (Namibia Dollar)"),
                            ("NGN", "NGN (Naira)"),
                            ("NIO", "NIO (Cordoba Oro)"),
                            ("NOK", "NOK (Norwegian Krone)"),
                            ("NPR", "NPR (Nepalese Rupee)"),
                            ("NZD", "NZD (New Zealand Dollar)"),
                            ("OMR", "OMR (Rial Omani)"),
                            ("PAB", "PAB (Balboa)"),
                            ("PEN", "PEN (Sol)"),
                            ("PGK", "PGK (Kina)"),
                            ("PHP", "PHP (Philippine Peso)"),
                            ("PKR", "PKR (Pakistan Rupee)"),
                            ("PLN", "PLN (Zloty)"),
                            ("PYG", "PYG (Guarani)"),
                            ("QAR", "QAR (Qatari Rial)"),
                            ("RON", "RON (Romanian Leu)"),
                            ("RSD", "RSD (Serbian Dinar)"),
                            ("RUB", "RUB (Russian Ruble)"),
                            ("RWF", "RWF (Rwanda Franc)"),
                            ("SAR", "SAR (Saudi Riyal)"),
                            ("SBD", "SBD (Solomon Islands Dollar)"),
                            ("SCR", "SCR (Seychelles Rupee)"),
                            ("SDG", "SDG (Sudanese Pound)"),
                            ("SEK", "SEK (Swedish Krona)"),
                            ("SGD", "SGD (Singapore Dollar)"),
                            ("SHP", "SHP (Saint Helena Pound)"),
                            ("SLL", "SLL (Leone)"),
                            ("SOS", "SOS (Somali Shilling)"),
                            ("SRD", "SRD (Surinam Dollar)"),
                            ("SSP", "SSP (South Sudanese Pound)"),
                            ("STD", "STD (Dobra)"),
                            ("SVC", "SVC (El Salvador Colon)"),
                            ("SYP", "SYP (Syrian Pound)"),
                            ("SZL", "SZL (Lilangeni)"),
                            ("THB", "THB (Baht)"),
                            ("TJS", "TJS (Somoni)"),
                            ("TMT", "TMT (Turkmenistan New Manat)"),
                            ("TND", "TND (Tunisian Dinar)"),
                            ("TOP", "TOP (Pa’anga)"),
                            ("TRY", "TRY (Turkish Lira)"),
                            ("TTD", "TTD (Trinidad and Tobago Dollar)"),
                            ("TWD", "TWD (New Taiwan Dollar)"),
                            ("TZS", "TZS (Tanzanian Shilling)"),
                            ("UAH", "UAH (Hryvnia)"),
                            ("UGX", "UGX (Uganda Shilling)"),
                            ("USD", "USD (US Dollar)"),
                            ("UYU", "UYU (Peso Uruguayo)"),
                            ("UZS", "UZS (Uzbekistan Sum)"),
                            ("VEF", "VEF (Bolívar)"),
                            ("VND", "VND (Dong)"),
                            ("VUV", "VUV (Vatu)"),
                            ("WST", "WST (Tala)"),
                            ("XAF", "XAF (CFA Franc BEAC)"),
                            ("XAG", "XAG (Silver)"),
                            ("XAU", "XAU (Gold)"),
                            (
                                "XBA",
                                "XBA (Bond Markets Unit European Composite Unit (EURCO))",
                            ),
                            (
                                "XBB",
                                "XBB (Bond Markets Unit European Monetary Unit (E.M.U.-6))",
                            ),
                            (
                                "XBC",
                                "XBC (Bond Markets Unit European Unit of Account 9 (E.U.A.-9))",
                            ),
                            (
                                "XBD",
                                "XBD (Bond Markets Unit European Unit of Account 17 (E.U.A.-17))",
                            ),
                            ("XCD", "XCD (East Caribbean Dollar)"),
                            ("XDR", "XDR (SDR (Special Drawing Right))"),
                            ("XOF", "XOF (CFA Franc BCEAO)"),
                            ("XPD", "XPD (Palladium)"),
                            ("XPF", "XPF (CFP Franc)"),
                            ("XPT", "XPT (Platinum)"),
                            ("XSU", "XSU (Sucre)"),
                            (
                                "XTS",
                                "XTS (Codes specifically reserved for testing purposes)",
                            ),
                            ("XUA", "XUA (ADB Unit of Account)"),
                            (
                                "XXX",
                                "XXX (The codes assigned for transactions where no currency is involved)",
                            ),
                            ("YER", "YER (Yemeni Rial)"),
                            ("ZAR", "ZAR (Rand)"),
                            ("ZMW", "ZMW (Zambian Kwacha)"),
                            ("ZWL", "ZWL (Zimbabwe Dollar)"),
                        ],
                        default="TZS",
                        help_text="The currency on which the subscription will be charged.",
                        max_length=5,
                    ),
                ),
                (
                    "trial_period_days",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Number of trial period days granted when             subscribing a customer to this plan.",
                        null=True,
                        verbose_name="Trial days",
                    ),
                ),
                (
                    "prebill_plan",
                    models.BooleanField(
                        help_text="If this is  set to True, then the plan base                 amount will be billed at the beginning of the                     billing cycle rather than after the end.",
                        null=True,
                    ),
                ),
                (
                    "enabled",
                    models.BooleanField(
                        default=True, help_text="Whether to accept subscription."
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
    ]
