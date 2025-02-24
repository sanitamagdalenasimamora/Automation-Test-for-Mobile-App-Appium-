*** Settings ***
Library           AppiumLibrary
Library           SeleniumLibrary

*** Variables ***
${REMOTE_URL}     http://localhost:4724/wd/hub
${PLATFORM_NAME}  Android
${DEVICE_NAME}    Google Nexus 4
${APP_PACKAGE}    com.lionparcel.mobile
${APP_ACTIVITY}   com.lionparcel.mobile.MainActivity

*** Test Cases ***

Scenario: Cek Tarif dengan Input Valid
    Given Membuka aplikasi lion parcel
    When Input asal pengiriman : "Jakarta Utara"
    And Input tujuan pengiriman : "Bekasi"
    And Input berat paket: 3
    And Klik tombol "Cek Tarif"
    Then Menampilkan jumlah tarif pengiriman

Scenario: Cek Tarif dengan Input Kosong
    Given Membuka aplikasi lion parce
    When Klik tombol "Cek Tarif"
    Then Error Validasi "Harap isi semua field"

*** Keywords ***

Membuka aplikasi Lion Parcel


Input asal pengiriman : ${asal}

Input tujuan pengiriman : ${tujuan}
    
Input berat paket : ${berat}

Klik tombol "Cek Tarif"

Menampilkan jumlah tarif pengiriman

Error Validasi "Harap isi semua field"