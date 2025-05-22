# 👕 FiveM AutoClothes Processor

## 🇧🇷 Visão Geral (Português)

Script Python para organizar automaticamente roupas mod no FiveM:

- Processa arquivos `.ydd`, `.ytd`, `.png` (imagem)
- Gera estrutura para Illenium Appearance
- Cria arquivos `.meta`, `fxmanifest.lua` e `diff_report.lua`
- Suporte a sobrescrita seletiva (`replace`)
- Múltiplos idiomas: 🇧🇷 pt, 🇺🇸 en, 🇪🇸 es, 🇫🇷 fr, 🇩🇪 de, 🇮🇹 it
- Compatível com servidores FiveM standalone ou ESX/QB

### ⚠️ Avisos importantes

- 💰 Você DEVE comprar uma licença Patron Argentum ou definir no server.cfg:

  ```
  sv_maxclients 8
  ```

  ...ou as roupas personalizadas não funcionarão.

- 📁 Todas as roupas devem estar em um único resource. Múltiplas pastas causarão conflito.
- 📦 Baixe roupas feitas para FiveM — evite .oiv e mods single player.
- ✅ Formatos válidos: .ydd, .ytd, .ymt, .meta
- ❌ Evite: .oiv, .rpf, etc.
- 🔗 Fonte recomendada: [https://www.gta5-mods.com/](https://www.gta5-mods.com/)

### 📝 Relatórios gerados

- `diff_report.lua`: mostra a quantidade e letras das texturas por item
- **Útil para configurar o YMT depois**

### 🧬 Requisito de YMT

Embora este script automatize a organização de arquivos e pastas, é necessário criar manualmente um arquivo `.ymt` para que as roupas possam ser selecionadas no Illenium Appearance.

👉 Siga este tutorial para entender como criar:
📺 [YMT Creation Tutorial by DRILLZ 3D](https://youtu.be/G3sLt5WFqtg?t=41)

🛠 Ferramenta recomendada:
[YMT Editor por grzybeek](https://github.com/grzybeek/YMTEditor)

---

## 🇺🇸 Overview (English)

Python script to auto-organize FiveM clothing mods:

- Processes `.ydd`, `.ytd`, `.png` files
- Creates folder layout for Illenium Appearance
- Generates `.meta`, `fxmanifest.lua` and `diff_report.lua`
- Supports selective `replace` by gender/category/index
- Fully multilingual: 🇧🇷 pt, 🇺🇸 en, 🇪🇸 es, 🇫🇷 fr, 🇩🇪 de, 🇮🇹 it

### ⚠️ Important Notes

- 💰 You MUST purchase a Patron Argentum license or set this in `server.cfg`:

  ```
  sv_maxclients 8
  ```

  ...or custom clothing will not work.

- 📁 All clothing must be in a single resource folder. No support for multiple clothing resources.
- 📦 Download clothing made for FiveM — avoid SP-only or .oiv mods.
- ✅ Valid formats: .ydd, .ytd, .ymt, .meta
- ❌ Avoid: .oiv, .rpf, etc.
- 🔗 Recommended source: [https://www.gta5-mods.com/](https://www.gta5-mods.com/)

### 📝 Reports generated

- `diff_report.lua`: shows quantity and letters of textures per item
- **Useful to configure YMT after**

### 🧬 YMT File Requirement

Although this script automates most folder and file organization, you must manually create a `.ymt` file to make clothing items selectable in Illenium Appearance.

👉 Follow this tutorial to understand how to create it:
📺 [YMT Creation Tutorial by DRILLZ 3D](https://youtu.be/G3sLt5WFqtg?t=41)

🛠 Recommended tool:
[YMT Editor by grzybeek](https://github.com/grzybeek/YMTEditor)

---

## 🇪🇸 Descripción (Español)

Script en Python para organizar mods de ropa en FiveM:

- Procesa archivos `.ydd`, `.ytd`, `.png`
- Crea carpetas y archivos para Illenium Appearance
- Genera `.meta`, `fxmanifest.lua` y `diff_report.lua`
- Compatible con `replace` por género/categoría/número

### ⚠️ Notas importantes

- 💰 Debes comprar una licencia Patron Argentum o definir en `server.cfg`:

  ```
  sv_maxclients 8
  ```

  ...o no funcionará la ropa personalizada.

- 📁 Toda la ropa debe estar en un único recurso. No se admite dividir por múltiples carpetas.
- 📦 Descarga ropa diseñada para FiveM — evita mods .oiv o para un solo jugador.
- ✅ Formatos válidos: .ydd, .ytd, .ymt, .meta
- ❌ Evita: .oiv, .rpf, etc.
- 🔗 Fuente recomendada: [https://www.gta5-mods.com/](https://www.gta5-mods.com/)

### 📝 Reportes generados

- `diff_report.lua`: muestra cantidad y letras de texturas por ítem
- **Útil para configurar el YMT luego**

### 🧬 Requisito de archivo YMT

Aunque este script automatiza gran parte de la organización, debes crear manualmente el archivo `.ymt` para que las prendas puedan seleccionarse en Illenium Appearance.

👉 Sigue este tutorial para aprender a crearlo:
📺 [YMT Creation Tutorial by DRILLZ 3D](https://youtu.be/G3sLt5WFqtg?t=41)

🛠 Herramienta recomendada:
[YMT Editor por grzybeek](https://github.com/grzybeek/YMTEditor)

---

## 🙌 Créditos / Credits

- 👨‍💻 Script by Chase
- 🧰 YMT Editor by grzybeek
- 🎓 Tutorial by DRILLZ 3D