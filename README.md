# 👻 GHOSTBYTE

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![13th Hour](https://img.shields.io/badge/13th%20Hour-Research-red.svg)]()

> *"Haunting the space between bytes."*

**GHOSTBYTE** is a comprehensive Unicode exploitation and ASCII art obfuscation toolkit for adversarial ML testing, security research, and red team operations. Generate invisible attacks, visual deceptions, and multi-layer encoding chains.

```
╔═══════════════════════════════════════════╗
║  👻 G H O S T B Y T E 👻                  ║
║  Unicode Exploit & Obfuscation Kit        ║
╚═══════════════════════════════════════════╝
```

## ⚠️ Ethical Use Notice

These tools are designed for:
- ✅ Security research and authorized red teaming
- ✅ Adversarial robustness testing in ML systems
- ✅ Educational purposes in application security
- ✅ Responsible disclosure programs

**Do not use for:**
- ❌ Malicious bypass of safety systems
- ❌ Unauthorized access to systems or data
- ❌ Generating harmful or deceptive content for fraud

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/frankSx/ghostbyte.git
cd ghostbyte

# Install
pip install -e .

# Run the demo
ghostbyte demo

# Generate homoglyph attack
ghostbyte unicode --text "admin" --mode homoglyph

# Create ASCII art payload
ghostbyte ascii --payload "sensitive" --mode box --style double

# Full obfuscation chain
ghostbyte chain --input "target" --config full
```

## 📦 Components

| Tool | Description | Use Case |
|------|-------------|----------|
| `unicode` | Homoglyphs, Bidi overrides, Zero-width chars | Tokenizer evasion, fingerprinting |
| `ascii` | ASCII art, glitch text, Zalgo | Visual deception, prompt injection |
| `mix` | Multi-layer encoding, polyglots | Deep obfuscation |
| `analyze` | Unicode analysis, risk scoring | Detection and forensics |
| `chain` | Full pipeline automation | Complete attack chains |

## 🎯 Attack Vectors

### Homoglyph Attacks
Replace Latin characters with visually identical Unicode look-alikes:
```
Visual: "password"
Actual: "pаsswоrd" (Cyrillic а = U+0430, о = U+043E)
```

### Bidirectional Overrides
Manipulate text direction to spoof file extensions or inject code:
```
Visual: "document.pdf"
Actual: "document‮fdp.exe‭" (with RLO/PDF controls)
```

### Zero-Width Fingerprinting
Embed invisible tracking data in leaked documents:
```python
from ghostbyte import GhostByte

gb = GhostByte()
marked = gb.fingerprint_embed("Q3 Revenue: $5.2M", user_id=1337)
# Document appears normal but contains tracker
```

## 📖 Documentation

- [Technical Write-up](docs/WRITEUP.md) - Deep dive into Unicode exploitation
- [Advanced Examples](examples/ADVANCED.md) - Complex attack chains
- [API Reference](docs/API.md) - Programmatic usage
- [Contributing](CONTRIBUTING.md) - How to contribute

## 🔬 Research Context

GHOSTBYTE was developed by **frankSx** as part of ongoing research into:
- Input validation bypass techniques in modern ML systems
- Tokenization edge cases in Large Language Models
- Visual spoofing in security-critical interfaces
- Cross-system Unicode normalization inconsistencies

**Author:** frankSx  
**Contact:** fixes.it.frank@googlesmail.com  
**Blog:** https://frankhacks.blogspot.com  
**Affiliation:** 13th Hour Research Division

## 🦀 The 13th Hour Principle

> *"In the liminal space between training and deployment, between input validation and model inference, we find the 13th Hour—a temporal metaphor for the overlooked moments where security assumptions fail."*

GHOSTBYTE operates in these liminal spaces:
- Between human visual perception and machine byte parsing
- Between intended functionality and emergent behavior
- Between validation layers and processing pipelines

## 📄 License

MIT License with Ethical Use Addendum - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- 13th Hour Research Division
- CTF and security research communities
- Unicode Consortium security guidelines
- Adversarial ML research community

---

*"Scare all the baby clwbots."* 🦀  
**© 2026 frankSx | fixes.it.frank@googlesmail.com**
