#!/usr/bin/env python3
"""
GHOSTBYTE String Mixer 👻
Combines multiple encoding strategies for maximum evasion

Author: frankSx <fixes.it.frank@googlesmail.com>
13th Hour Research Division
"""

import argparse
import base64
import random
import hashlib


class StringMixer:
    """Combines multiple obfuscation techniques - GHOSTBYTE"""

    def __init__(self, seed: int = None):
        if seed:
            random.seed(seed)
        self.techniques = {
            'base64': self._base64_encode,
            'rot13': self._rot13,
            'reverse': self._reverse,
            'hex': self._hex_encode,
            'url': self._url_encode,
            'binary': self._binary_encode,
        }

    def _base64_encode(self, s: str) -> str:
        return base64.b64encode(s.encode()).decode()

    def _rot13(self, s: str) -> str:
        return s.translate(str.maketrans(
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
            'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
        ))

    def _reverse(self, s: str) -> str:
        return s[::-1]

    def _hex_encode(self, s: str) -> str:
        return s.encode().hex()

    def _url_encode(self, s: str) -> str:
        return ''.join(f'%{ord(c):02x}' if ord(c) > 127 or c in ' %&=' else c for c in s)

    def _binary_encode(self, s: str) -> str:
        return ' '.join(format(ord(c), '08b') for c in s)

    def mix(self, text: str, layers: int = 3, techniques: list = None):
        """Apply multiple encoding layers"""
        if techniques is None:
            techniques = random.sample(list(self.techniques.keys()), min(layers, len(self.techniques)))

        current = text
        history = [('original', text)]

        for tech in techniques[:layers]:
            if tech in self.techniques:
                current = self.techniques[tech](current)
                history.append((tech, current))

        return {
            'original': text,
            'final': current,
            'layers': len(history) - 1,
            'techniques': [h[0] for h in history[1:]],
            'history': history,
            'hash': hashlib.sha256(current.encode()).hexdigest()[:16]
        }

    def create_polyglot(self, text: str) -> str:
        """Create a polyglot that works in multiple contexts"""
        lines = [
            '#!/bin/sh',
            '/*',
            ':',
            text,
            '*/',
            'echo "' + text + '"'
        ]
        return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='GHOSTBYTE String Mixer 👻')
    parser.add_argument('--input', required=True)
    parser.add_argument('--layers', type=int, default=3)
    parser.add_argument('--techniques', nargs='+')
    parser.add_argument('--mode', choices=['mix', 'polyglot'], default='mix')
    parser.add_argument('--output')

    args = parser.parse_args()

    mixer = StringMixer()

    if args.mode == 'mix':
        result = mixer.mix(args.input, args.layers, args.techniques)
        output = f"""👻 GHOSTBYTE Mixed String
Original: {result['original']}
Final: {result['final']}
Layers: {result['layers']}
Techniques: {', '.join(result['techniques'])}
Hash: {result['hash']}"""
    elif args.mode == 'polyglot':
        output = mixer.create_polyglot(args.input)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"👻 Output written to {args.output}")
    else:
        print(output)


if __name__ == '__main__':
    main()
