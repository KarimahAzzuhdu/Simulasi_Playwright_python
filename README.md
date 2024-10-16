# **Simulasi QA - Automation Test**
Sama seperti repo [Simulasi Playwright](https://github.com/KarimahAzzuhdu/Simulasi_Playwright), proyek ini adalah simulasi pekerjaan Quality Assurance (QA) mulai dari perencanaan hingga pelaporan. Bedanya bahasa yang digunakan untuk Python dan web demo publik yang dipakai [OrangeHRM](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login). Tujuan utama dilakukan proyek ini untuk latihan QA Automation Test dan membandingkan penggunaan Playwright Python dengan Javascript.

---

## **Automation Web UI Test Plan**

Secara garis besar sama isinya dengan [Test Plan Simulasi Playwright](https://github.com/KarimahAzzuhdu/Simulasi_Playwright/blob/main/README.md), jadi disini hanya fokus ke spesifik plan seperti test items, scenario, dan case saja.

#### **1. *Test Items***
##### Fitur pada situs web yang akan diuji :
- **Login**
- *to be decided later*

#### **2. *Test Environment & Test Data***
##### Test Environment :
   - **Browser:** Chromium
   - **Sistem Operasi:** Windows
   - **Perangkat:** Desktop
##### Test Data :
| Username | Password |
|----------|----------|
| Admin    | admin123|

#### **3. *Test Scenarios & Test Cases***
##### **Login**
- Test Scenario : Memverifikasi alur login/logout dengan kredensial yang valid dan tidak valid di halaman Login.
- *Prerequisites condition* : user already registered

| Test ID  | Test Case Description | Expected Outcome |
|----------|-----------------------|------------------|
| TC_LOG_1 | Verify Login Process with valid credentials | User successfully logs in and redirected to Dashboard Page |
| TC_LOG_2 | Verify Logout Process | User successfully logs out and redirected to Login Page |
| TC_LOG_3 | Verify error message for Login with invalid credentials | Displays error message |
| TC_LOG_4 | Verify error message for Login with blank field | Displays "required" message at the blank field |
| TC_LOG_5 | Verify Forgot Password Process | User successfully reset their password |