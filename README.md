# Portfolio

## Ishqa túsiriw

Windows-ta joybar papkasındaǵı `start.bat` faylın iske túsiriń. Yaki PowerShell-da:

```powershell
python -m pip install -r requirements.txt
python backend\app.py
```

Server kompyuterde `http://localhost:5000` adresinde isleyedi. Telefon menen
bir Wi-Fi tarmaǵında bolǵanda, kompyuterińizdiń jergilikli IP adresin
`http://<kompyuter-IP>:5000` túrinde telefonda ashıń. Mısalı:
`http://192.168.1.22:5000`. IP routerge qarap ózgeriwi múmkin; PowerShell-da
`Get-NetIPAddress -AddressFamily IPv4` buyırıǵı menen tekseriń.

Bul ashıq sayt bir jergilikli tarmaqtaǵı qurılmalarǵa kórinedi. Tek ózińiz
isenetuǵın Wi-Fi tarmaǵında qollanıń hám routerde port forwarding qospаń;
registraciya hám kiriw alıp taslanǵan.

## Bólimler

- Portfolio: `/portfolio-winter2`
- Ashıq oyınlar dizimi: `/game/`
- Server jaǵdayı: `/api/health`

Oyınlar `frontend\game` papkasındaǵı HTML fayllarınan avtomat túrde kórsetiledi.
Registraciya, parol menen kiriw, RSA/FIDO2/WebAuthn autentifikaciyası,
paydalanıwshı akkauntları hám olardıń maǵlıwmat bazaları joybardıń ishinen alıp tastaldı.
