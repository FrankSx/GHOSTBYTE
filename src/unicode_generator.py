#!/usr/bin/env python3
"""
GHOSTBYTE Unicode Generator 👻
Generates various Unicode-based adversarial strings

Author: frankSx <fixes.it.frank@googlesmail.com>
13th Hour Research Division

Part of the GHOSTBYTE toolkit for adversarial ML testing.
"""

import argparse
import random
import unicodedata
from typing import List, Dict, Optional

# Homoglyph mappings (Latin look-alikes)
HOMOGLYPH_MAP = {
    'a': ['а', 'а', 'α', 'а', 'а'],
    'b': ['Ь', 'ь', 'β', 'в'],
    'c': ['с', 'с', '¢', 'с'],
    'd': ['ԁ', 'ɗ', 'đ'],
    'e': ['е', 'е', 'ε', 'е', 'е'],
    'f': ['ƒ', 'ϝ', 'ḟ'],
    'g': ['ɡ', 'ց', 'ǵ'],
    'h': ['һ', 'һ', 'ћ', 'ḧ'],
    'i': ['і', 'і', 'ι', 'і', 'і'],
    'j': ['ј', 'ј', 'ʝ', 'ϳ'],
    'k': ['κ', 'к', 'ḱ', 'к'],
    'l': ['ⅼ', 'ℓ', 'ḻ', 'ł'],
    'm': ['м', 'м', 'ṃ', 'м'],
    'n': ['ո', 'η', 'ṅ', 'ń'],
    'o': ['о', 'о', 'ο', 'о', 'о'],
    'p': ['р', 'р', 'ρ', 'р', 'р'],
    'q': ['ԛ', 'գ', 'զ'],
    'r': ['г', 'г', 'ṛ', 'г'],
    's': ['ѕ', 'ѕ', 'ṡ', 'ś'],
    't': ['т', 'т', 'τ', 'ṫ'],
    'u': ['υ', 'μ', 'ṵ', 'ú'],
    'v': ['ν', 'ν', 'ν', 'ν'],
    'w': ['ω', 'ш', 'ẃ', 'ŵ'],
    'x': ['х', 'х', 'χ', 'х', '×'],
    'y': ['у', 'у', 'γ', 'ý'],
    'z': ['ᴢ', 'ž', 'ź', 'ż'],
}

ZWS = '\u200B'
ZWNJ = '\u200C'
ZWJ = '\u200D'
BOM = '\uFEFF'
LRE = '\u202A'
RLE = '\u202B'
PDF = '\u202C'
LRO = '\u202D'
RLO = '\u202E'


class UnicodeExploitGenerator:
    """Generator for Unicode-based adversarial strings - GHOSTBYTE"""

    def __init__(self, seed: Optional[int] = None):
        if seed:
            random.seed(seed)

    def homoglyph_replace(self, text: str, intensity: float = 0.5) -> str:
        """Replace Latin characters with visually similar Unicode homoglyphs"""
        result = []
        for char in text.lower():
            if char in HOMOGLYPH_MAP and random.random() < intensity:
                replacement = random.choice(HOMOGLYPH_MAP[char])
                result.append(replacement)
            else:
                result.append(char)
        return ''.join(result)

    def insert_zero_width(self, text: str, density: float = 0.3) -> str:
        """Insert zero-width characters throughout text"""
        zw_chars = [ZWS, ZWNJ, ZWJ, BOM]
        result = []
        for char in text:
            result.append(char)
            if random.random() < density:
                result.append(random.choice(zw_chars))
        return ''.join(result)

    def bidi_override(self, text: str, mode: str = 'rtl') -> str:
        """Wrap text with bidirectional overrides"""
        if mode == 'rtl':
            return RLO + text + PDF
        else:
            return LRO + text + PDF

    def bidi_embed(self, text: str, inject: str, position: Optional[int] = None) -> str:
        """Embed text with different directionality"""
        if position is None:
            position = len(text) // 2
        embedded = RLE + inject + PDF
        return text[:position] + embedded + text[position:]

    def confusable_mix(self, text: str) -> str:
        """Create maximum confusion with mixed strategies"""
        text = self.homoglyph_replace(text, intensity=0.7)
        text = self.insert_zero_width(text, density=0.2)
        text = self.bidi_override(text[:len(text)//2], 'ltr') + text[len(text)//2:]
        return text

    def fingerprint_embed(self, text: str, identifier: int) -> str:
        """Embed invisible fingerprint using zero-width chars"""
        binary = bin(identifier)[2:].zfill(32)
        fingerprint = ''
        for bit in binary:
            fingerprint += ZWJ if bit == '1' else ZWNJ
        pos = random.randint(0, len(text))
        return text[:pos] + fingerprint + text[pos:]

    def extract_fingerprint(self, text: str) -> Optional[int]:
        """Extract fingerprint from text"""
        binary = ''
        for char in text:
            if char == ZWJ:
                binary += '1'
            elif char == ZWNJ:
                binary += '0'
        if len(binary) >= 32:
            return int(binary[:32], 2)
        return None

    def normalization_attack(self, text: str) -> Dict[str, str]:
        """Generate different normalization forms"""
        return {
            'original': text,
            'nfc': unicodedata.normalize('NFC', text),
            'nfd': unicodedata.normalize('NFD', text),
            'nfkc': unicodedata.normalize('NFKC', text),
            'nfkd': unicodedata.normalize('NFKD', text),
        }

    def ascii_art_payload(self, payload: str, style: str = 'block') -> str:
        """Create ASCII art that encodes a payload"""
        if style == 'block':
            lines = [
                '┌' + '─' * (len(payload) + 2) + '┐',
                '│ ' + payload + ' │',
                '└' + '─' * (len(payload) + 2) + '┘'
            ]
        elif style == 'banner':
            lines = [
                '╔' + '═' * (len(payload) + 2) + '╗',
                '║ ' + payload + ' ║',
                '╚' + '═' * (len(payload) + 2) + '╝'
            ]
        elif style == 'matrix':
            lines = [
                '▓' * (len(payload) + 4),
                '▓ ' + payload + ' ▓',
                '▓' * (len(payload) + 4)
            ]
        else:
            lines = [payload]
        return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='GHOSTBYTE Unicode Generator 👻'
    )
    parser.add_argument('--text', required=True, help='Input text')
    parser.add_argument('--mode', choices=[
        'homoglyph', 'zerowidth', 'bidi', 'confusable', 
        'fingerprint', 'normalize', 'asciiart'
    ], required=True)
    parser.add_argument('--intensity', type=float, default=0.5)
    parser.add_argument('--seed', type=int)
    parser.add_argument('--output')
    parser.add_argument('--id', type=int)
    parser.add_argument('--style', default='block')

    args = parser.parse_args()

    gen = UnicodeExploitGenerator(seed=args.seed)

    if args.mode == 'homoglyph':
        result = gen.homoglyph_replace(args.text, args.intensity)
    elif args.mode == 'zerowidth':
        result = gen.insert_zero_width(args.text, args.intensity)
    elif args.mode == 'bidi':
        result = gen.bidi_override(args.text, 'rtl')
    elif args.mode == 'confusable':
        result = gen.confusable_mix(args.text)
    elif args.mode == 'fingerprint':
        identifier = args.id or 12345
        result = gen.fingerprint_embed(args.text, identifier)
        print(f"👻 Embedded fingerprint ID: {identifier}", file=__import__('sys').stderr)
    elif args.mode == 'normalize':
        results = gen.normalization_attack(args.text)
        result = '\n'.join([f"{k}: {v}" for k, v in results.items()])
    elif args.mode == 'asciiart':
        result = gen.ascii_art_payload(args.text, args.style)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"👻 Output written to {args.output}")
    else:
        print(result)


if __name__ == '__main__':
    main()
