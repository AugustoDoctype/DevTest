Página de código ativa: 65001

C:\Users\pedro\OneDrive\Documentos\pedra_papel_tesoura> python --version
Python 3.13.15

C:\Users\pedro\OneDrive\Documentos\pedra_papel_tesoura> python -m venv ambiente

C:\Users\pedro\OneDrive\Documentos\pedra_papel_tesoura> powershell -ExecutionPolicy Bypass
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\pedro\OneDrive\Documentos\pedra_papel_tesoura> . .\ambiente\Scripts\Activate
(ambiente) PS C:\Users\pedro\OneDrive\Documentos\pedra_papel_tesoura> pip install pytest
Collecting pytest
  Using cached pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)
Collecting colorama>=0.4 (from pytest)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting iniconfig>=1.0.1 (from pytest)
  Using cached iniconfig-2.3.0-py3-none-any.whl.metadata (2.5 kB)
Collecting packaging>=22 (from pytest)
  Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pluggy<2,>=1.5 (from pytest)
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting pygments>=2.7.2 (from pytest)
  Using cached pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
Using cached pytest-9.1.1-py3-none-any.whl (386 kB)
Using cached pluggy-1.6.0-py3-none-any.whl (20 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Using cached iniconfig-2.3.0-py3-none-any.whl (7.5 kB)
Using cached packaging-26.3-py3-none-any.whl (129 kB)
Using cached pygments-2.21.0-py3-none-any.whl (1.3 MB)
Installing collected packages: pygments, pluggy, packaging, iniconfig, colorama, pytest
Successfully installed colorama-0.4.6 iniconfig-2.3.0 packaging-26.3 pluggy-1.6.0 pygments-2.21.0 pytest-9.1.1
(ambiente) PS C:\Users\pedro\OneDrive\Documentos\pedra_papel_tesoura> pytest

========================================================= test session starts ==========================================================
platform win32 -- Python 3.13.15, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\pedro\OneDrive\Documentos\pedra_papel_tesoura
collected 1 item                                                                                                                        

test_jogo.py .                                                                                                                    [100%]

========================================================== 1 passed in 0.03s ===========================================================
(ambiente) PS C:\Users\pedro\OneDrive\Documentos\pedra_papel_tesoura> python app.py
=== Pedra, Papel ou Tesoura ===
Escolha pedra, papel ou tesoura: pedra
Computador escolheu: papel
Computador venceu

(ambiente) PS C:\Users\pedro\OneDrive\Documentos\pedra_papel_tesoura> python app.py
=== Pedra, Papel ou Tesoura ===
Escolha pedra, papel ou tesoura: papel
Computador escolheu: tesoura
Computador venceu

(ambiente) PS C:\Users\pedro\OneDrive\Documentos\pedra_papel_tesoura> python app.py
=== Pedra, Papel ou Tesoura ===
Escolha pedra, papel ou tesoura: tesoura
Computador escolheu: papel
Você venceu