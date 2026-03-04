"""
GHOSTBYTE 👻
Unicode Exploit & ASCII Obfuscation Toolkit

Author: frankSx <fixes.it.frank@googlesmail.com>
13th Hour Research Division

A comprehensive toolkit for adversarial ML testing using Unicode manipulation
and ASCII art obfuscation techniques.
"""

__version__ = "1.0.0"
__author__ = "frankSx"
__email__ = "fixes.it.frank@googlesmail.com"
__license__ = "MIT with Ethical Use Addendum"

from .unicode_generator import UnicodeExploitGenerator
from .ascii_obfuscator import ASCIIObfuscator
from .string_mixer import StringMixer
from .unicode_analyzer import UnicodeAnalyzer


class GhostByte:
    """
    Main GHOSTBYTE interface combining all toolkit functionality.

    Usage:
        gb = GhostByte()

        # Unicode exploits
        obfuscated = gb.homoglyph_replace("admin", intensity=0.7)
        fingerprinted = gb.fingerprint_embed("secret", user_id=1234)

        # ASCII obfuscation
        art = gb.create_box("payload", style="double")
        glitched = gb.create_glitch_text("text")

        # Analysis
        analysis = gb.analyze("suspicious string")
    """

    def __init__(self, seed: int = None):
        """
        Initialize GHOSTBYTE toolkit.

        Args:
            seed: Optional random seed for reproducible results
        """
        self.unicode_gen = UnicodeExploitGenerator(seed=seed)
        self.ascii_obf = ASCIIObfuscator(seed=seed)
        self.mixer = StringMixer(seed=seed)
        self.analyzer = UnicodeAnalyzer()

    # Unicode methods
    def homoglyph_replace(self, text: str, intensity: float = 0.5) -> str:
        """Replace characters with Unicode homoglyphs"""
        return self.unicode_gen.homoglyph_replace(text, intensity)

    def insert_zero_width(self, text: str, density: float = 0.3) -> str:
        """Insert zero-width characters throughout text"""
        return self.unicode_gen.insert_zero_width(text, density)

    def bidi_override(self, text: str, mode: str = 'rtl') -> str:
        """Wrap text with bidirectional overrides"""
        return self.unicode_gen.bidi_override(text, mode)

    def confusable_mix(self, text: str) -> str:
        """Apply maximum confusion mixing"""
        return self.unicode_gen.confusable_mix(text)

    def fingerprint_embed(self, text: str, identifier: int) -> str:
        """Embed invisible fingerprint in text"""
        return self.unicode_gen.fingerprint_embed(text, identifier)

    def fingerprint_extract(self, text: str) -> int:
        """Extract fingerprint from text"""
        return self.unicode_gen.extract_fingerprint(text)

    # ASCII methods
    def create_box(self, content: str, style: str = 'single', padding: int = 1) -> str:
        """Create box around content"""
        return self.ascii_obf.create_box(content, style, padding)

    def create_banner(self, content: str, style: str = 'double') -> str:
        """Create banner-style box"""
        return self.ascii_obf.create_banner(content, style)

    def create_glitch_text(self, text: str, intensity: float = 0.3) -> str:
        """Create glitchy-looking text"""
        return self.ascii_obf.create_glitch_text(text, intensity)

    def create_zalgo(self, text: str, intensity: int = 3) -> str:
        """Create Zalgo-style text"""
        return self.ascii_obf.create_zalgo(text, intensity)

    def create_matrix_rain(self, width: int = 40, height: int = 10) -> str:
        """Create matrix-style rain effect"""
        return self.ascii_obf.create_matrix_rain(width, height)

    # Mixing methods
    def mix_encode(self, text: str, layers: int = 3, techniques: list = None) -> dict:
        """Apply multi-layer encoding"""
        return self.mixer.mix(text, layers, techniques)

    def create_polyglot(self, text: str) -> str:
        """Create multi-context polyglot"""
        return self.mixer.create_polyglot(text)

    # Analysis methods
    def analyze(self, text: str) -> dict:
        """Analyze text for Unicode issues"""
        return self.analyzer.analyze(text)

    def generate_report(self, analysis: dict) -> str:
        """Generate human-readable report"""
        return self.analyzer.generate_report(analysis)

    # Chain methods
    def obfuscate_chain(self, text: str, config: str = 'medium') -> dict:
        """
        Run full obfuscation chain.

        Args:
            text: Input text
            config: 'light', 'medium', 'full', or 'extreme'
        """
        configs = {
            'light': {'homoglyph': 0.3, 'zw': 0.1, 'layers': 2},
            'medium': {'homoglyph': 0.5, 'zw': 0.3, 'layers': 3},
            'full': {'homoglyph': 0.8, 'zw': 0.5, 'layers': 4},
            'extreme': {'homoglyph': 1.0, 'zw': 0.8, 'layers': 5}
        }

        cfg = configs.get(config, configs['medium'])

        # Apply chain
        step1 = self.homoglyph_replace(text, cfg['homoglyph'])
        step2 = self.insert_zero_width(step1, cfg['zw'])
        step3 = self.create_box(step2, style='double')
        step4 = self.mix_encode(step3, layers=cfg['layers'])

        return {
            'original': text,
            'final': step4['final'],
            'config': config,
            'steps': ['homoglyph', 'zero_width', 'ascii_box', 'mixed'],
            'expansion_ratio': len(step4['final']) / len(text)
        }


# Convenience functions for direct usage
def homoglyph(text: str, intensity: float = 0.5) -> str:
    """Quick homoglyph replacement"""
    return GhostByte().homoglyph_replace(text, intensity)


def glitch(text: str, intensity: float = 0.3) -> str:
    """Quick glitch text generation"""
    return GhostByte().create_glitch_text(text, intensity)


def analyze(text: str) -> dict:
    """Quick text analysis"""
    return GhostByte().analyze(text)


__all__ = [
    'GhostByte',
    'UnicodeExploitGenerator',
    'ASCIIObfuscator', 
    'StringMixer',
    'UnicodeAnalyzer',
    'homoglyph',
    'glitch',
    'analyze',
]
