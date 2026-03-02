# 🎨 Recursos CustomTkinter Utilizados

Este documento detalha os componentes e recursos da biblioteca **CustomTkinter** utilizados no Upper Tone.

## 📚 Sobre CustomTkinter

CustomTkinter é uma biblioteca Python moderna baseada em Tkinter que oferece widgets personalizados com aparência profissional e temas dark/light.

**Site oficial:** https://github.com/TomSchimansky/CustomTkinter

---

## 🧩 Componentes Utilizados

### CTk (Janela Principal)
```python
app = ctk.CTk()
```
- Substitui `tk.Tk()` do tkinter tradicional
- Suporte automático a temas dark/light
- Melhor renderização de elementos

### CTkFrame
```python
ctk.CTkFrame(parent, corner_radius=15, fg_color="#2b2b2b")
```
- Frames com cantos arredondados
- Controle total de cores de fundo
- Suporte a transparência

**Uso no Upper Tone:**
- Cards das seções 1, 2 e 3
- Frame principal da aplicação
- Containers para organização de elementos

### CTkLabel
```python
ctk.CTkLabel(parent, text="Upper Tone", font=ctk.CTkFont(size=36, weight="bold"))
```
- Labels com suporte a fontes customizadas
- Cores de texto configuráveis para modo dark/light
- Alinhamento e wrapping de texto

**Uso no Upper Tone:**
- Título principal "Upper Tone"
- Subtítulo descritivo
- Badges numerados (1, 2, 3)
- Textos de cada seção
- Status bar
- Preview do valor do slider

### CTkButton
```python
ctk.CTkButton(
    parent,
    text="Processar Arquivo",
    command=callback,
    height=50,
    corner_radius=12,
    fg_color="#16a34a",
    hover_color="#15803d"
)
```
- Botões modernos com efeito hover
- Cantos arredondados configuráveis
- Estados (normal, disabled, hover)
- Cores personalizáveis

**Uso no Upper Tone:**
- Botão "Escolher Arquivo Musical" (azul)
- Botão "🚀 Processar Arquivo" (verde)
- Botão "OK" no diálogo de sucesso

### CTkSlider
```python
ctk.CTkSlider(
    parent,
    from_=1,
    to=11,
    number_of_steps=10,
    command=update_callback
)
```
- Slider moderno e responsivo
- Callback em tempo real
- Cores de progresso customizáveis
- Botão circular arrastável

**Uso no Upper Tone:**
- Seleção de quantidade de semitons (1-11)
- Atualização em tempo real do valor exibido

### CTkRadioButton
```python
ctk.CTkRadioButton(
    parent,
    text="Subir Tom",
    variable=string_var,
    value="subir"
)
```
- Radio buttons modernos
- Maior área clicável
- Visual consistente com o tema

**Uso no Upper Tone:**
- Seleção de direção: "Subir Tom" ou "Descer Tom"

### CTkFont
```python
ctk.CTkFont(family="Helvetica", size=36, weight="bold")
```
- Fontes customizadas com peso configurável
- Suporte cross-platform
- Tamanhos e estilos flexíveis

**Uso no Upper Tone:**
- Diferentes tamanhos para hierarquia visual
- Bold para títulos e botões
- Normal para textos descritivos

### CTkToplevel
```python
dialog = ctk.CTkToplevel()
```
- Janelas de diálogo modernas
- Modal e transiente
- Mesma aparência da janela principal

**Uso no Upper Tone:**
- Diálogo de sucesso após processamento

---

## 🎨 Configurações Globais

### Modo de Aparência
```python
ctk.set_appearance_mode("dark")
```
- `"dark"` - Sempre modo escuro
- `"light"` - Sempre modo claro
- `"system"` - Segue o sistema operacional

**Upper Tone:** Usa modo `"dark"` para aparência profissional

### Tema de Cores
```python
ctk.set_default_color_theme("blue")
```
- `"blue"` - Tema azul (padrão)
- `"dark-blue"` - Azul escuro
- `"green"` - Tema verde

**Upper Tone:** Usa tema `"blue"` com customizações adicionais

---

## 🎨 Paleta de Cores do Upper Tone

### Cores Principais
- **Azul Primário:** `#1f6aa5` / `#3b8ed0` (light/dark)
- **Verde Sucesso:** `#16a34a` / `#22c55e`
- **Laranja Processando:** `#d97706` / `#f59e0b`
- **Cinza Fundo:** `#2b2b2b`
- **Cinza Status:** `#1a1a1a`

### Esquema de Cores por Estado
- ✅ **Sucesso:** Verde (`#16a34a`)
- ⏳ **Processando:** Laranja (`#d97706`)
- 🔵 **Normal:** Azul (`#1f6aa5`)
- ⚪ **Neutro:** Cinza (`gray70`)

---

## 💡 Boas Práticas Aplicadas

1. **Consistência Visual**
   - Mesmos corner_radius em todos os cards (15px)
   - Mesma altura para botões principais (42-50px)
   - Padding uniforme (20px interno, 25px externo)

2. **Hierarquia de Cores**
   - Azul para ações principais
   - Verde para ação final (processar)
   - Cinza para containers e fundo

3. **Responsividade**
   - Uso de `pack(fill='x')` para largura responsiva
   - Widgets expandem com o container pai

4. **Feedback Visual**
   - Cores mudam baseado no estado
   - Hover effects em botões
   - Cursor muda para 'hand2' em elementos clicáveis

5. **Acessibilidade**
   - Alto contraste texto/fundo
   - Elementos grandes e fáceis de clicar
   - Feedback claro em cada ação

---

## 📖 Recursos Úteis

- [Documentação CustomTkinter](https://customtkinter.tomschimansky.com/)
- [GitHub CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Exemplos de Código](https://github.com/TomSchimansky/CustomTkinter/tree/master/examples)

---

## 🔄 Migração de Tkinter para CustomTkinter

### Diferenças Principais

| Tkinter | CustomTkinter |
|---------|---------------|
| `tk.Tk()` | `ctk.CTk()` |
| `tk.Frame()` | `ctk.CTkFrame()` |
| `tk.Label()` | `ctk.CTkLabel()` |
| `tk.Button()` | `ctk.CTkButton()` |
| `tk.Entry()` | `ctk.CTkEntry()` |
| `font=('Arial', 12)` | `font=ctk.CTkFont(size=12)` |
| `bg=`, `fg=` | `fg_color=`, `text_color=` |

### Vantagens do CustomTkinter

✅ Visual moderno out-of-the-box  
✅ Tema dark/light automático  
✅ Widgets arredondados  
✅ Efeitos hover nativos  
✅ Melhor cross-platform  
✅ Mais fácil de estilizar  
✅ Performance melhorada  

---

**Este documento serve como referência para futuras atualizações e novos desenvolvedores que trabalharão no projeto.**
