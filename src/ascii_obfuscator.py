#!/usr/bin/env python3
"""
GHOSTBYTE ASCII Obfuscator 👻
Creates visually deceptive ASCII art for adversarial testing

Author: frankSx <fixes.it.frank@googlesmail.com>
13th Hour Research Division
"""

import argparse
import base64
import random


class ASCIIObfuscator:
    """Creates ASCII art with hidden payloads - GHOSTBYTE"""

    BOX_STYLES = {
        'single': {'h': '─', 'v': '│', 'tl': '┌', 'tr': '┐', 'bl': '└', 'br': '┘'},
        'double': {'h': '═', 'v': '║', 'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝'},
        'round': {'h': '─', 'v': '│', 'tl': '╭', 'tr': '╮', 'bl': '╰', 'br': '╯'},
        'bold': {'h': '━', 'v': '┃', 'tl': '┏', 'tr': '┓', 'bl': '┗', 'br': '┛'},
    }

    SHADING = ['░', '▒', '▓', '█', '▀', '▄', '▌', '▐']

    def __init__(self, seed: int = None):
        if seed:
            random.seed(seed)

    def create_box(self, content: str, style: str = 'single', padding: int = 1) -> str:
        """Create a box around content"""
        chars = self.BOX_STYLES.get(style, self.BOX_STYLES['single'])
        width = len(content) + (padding * 2)

        top = chars['tl'] + chars['h'] * width + chars['tr']
        middle = chars['v'] + ' ' * padding + content + ' ' * padding + chars['v']
        bottom = chars['bl'] + chars['h'] * width + chars['br']

        return '\n'.join([top, middle, bottom])

    def create_banner(self, content: str, style: str = 'double') -> str:
        """Create a banner-style box"""
        return self.create_box(content.upper(), style, padding=2)

    def create_matrix_rain(self, width: int = 40, height: int = 10, density: float = 0.3) -> str:
        """Create matrix-style falling characters"""
        katakana = [chr(i) for i in range(0xFF66, 0xFF9D)]
        digits = [str(i) for i in range(10)]
        chars = katakana + digits

        lines = []
        for _ in range(height):
            line = ''
            for _ in range(width):
                if random.random() < density:
                    line += random.choice(chars)
                else:
                    line += ' '
            lines.append(line)
        return '\n'.join(lines)

    def embed_in_art(self, payload: str, art_type: str = 'random') -> str:
        """Embed a payload within decorative ASCII art"""
        if art_type == 'random':
            art_type = random.choice(['border', 'shading', 'matrix'])

        if art_type == 'border':
            return self._embed_border(payload)
        elif art_type == 'shading':
            return self._embed_shading(payload)
        else:
            return self._embed_matrix(payload)

    def _embed_border(self, payload: str) -> str:
        """Embed payload in border decorations"""
        encoded = base64.b64encode(payload.encode()).decode()
        width = max(len(payload), 20)

        lines = [
            '┌' + '─' * width + '┐',
            '│' + ' ' * ((width - len(payload)) // 2) + payload + ' ' * ((width - len(payload)) // 2) + '│',
            '├' + '─' * width + '┤'
        ]

        for i in range(0, len(encoded), width-2):
            chunk = encoded[i:i+width-2]
            lines.append('│ ' + chunk.ljust(width-2) + ' │')

        lines.append('└' + '─' * width + '┘')
        return '\n'.join(lines)

    def _embed_shading(self, payload: str) -> str:
        """Embed payload using shading characters"""
        binary = ''.join(format(ord(c), '08b') for c in payload)
        width = 16
        height = (len(binary) + width - 1) // width

        lines = []
        idx = 0
        for _ in range(height):
            line = ''
            for _ in range(width):
                if idx < len(binary):
                    char = self.SHADING[0] if binary[idx] == '0' else self.SHADING[3]
                    line += char
                    idx += 1
                else:
                    line += self.SHADING[1]
            lines.append(line)
        return '\n'.join(lines)

    def _embed_matrix(self, payload: str) -> str:
        """Embed payload in matrix-style frame"""
        width = len(payload) + 6
        lines = [
            '▓' * width,
            '▓' + '░' * (width-2) + '▓',
            '▓░ ' + payload + ' ░▓',
            '▓' + '░' * (width-2) + '▓',
            '▓' * width
        ]
        return '\n'.join(lines)

    def create_glitch_text(self, text: str, intensity: float = 0.3) -> str:
        """Create glitchy-looking text"""
        glitch_chars = ['̷', '̸', '̶', '̵', '̴', '̲', '̅', '̈', '̇', '̣']

        result = []
        for char in text:
            result.append(char)
            if random.random() < intensity:
                result.append(random.choice(glitch_chars))
        return ''.join(result)

    def create_zalgo(self, text: str, intensity: int = 3) -> str:
        """Create Zalgo-style combining character text"""
        combining = [
            '\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305',
            '\u0306', '\u0307', '\u0308', '\u0309', '\u030A', '\u030B',
            '\u030C', '\u030D', '\u030E', '\u030F'
        ]

        result = []
        for char in text:
            result.append(char)
            for _ in range(random.randint(0, intensity)):
                result.append(random.choice(combining))
        return ''.join(result)

    def ghostbyte_logo(self) -> str:
        """Return GHOSTBYTE ASCII logo"""
        return '''
    ╔═╗┬ ┌─┐┌─┐┌┬┐╔╗ ┬ ┌┬┐┌─┐
    ║ ╦│ │ ├┤  │ ╠╩╗│  │ ├┤
    ╚═╝┴ └─┘└─┘ ┴ ╚═╝┴  ┴ └─┘
       👻 G H O S T B Y T E 👻
        '''


def main():
    parser = argparse.ArgumentParser(description='GHOSTBYTE ASCII Obfuscator 👻')
    parser.add_argument('--payload', required=True)
    parser.add_argument('--mode', choices=['box', 'banner', 'matrix', 'embed', 'glitch', 'zalgo', 'logo'], default='box')
    parser.add_argument('--style', default='single')
    parser.add_argument('--seed', type=int)
    parser.add_argument('--output')

    args = parser.parse_args()

    obf = ASCIIObfuscator(seed=args.seed)

    if args.mode == 'box':
        result = obf.create_box(args.payload, args.style)
    elif args.mode == 'banner':
        result = obf.create_banner(args.payload, args.style)
    elif args.mode == 'matrix':
        result = obf.create_matrix_rain(width=len(args.payload)+10, height=5)
    elif args.mode == 'embed':
        result = obf.embed_in_art(args.payload)
    elif args.mode == 'glitch':
        result = obf.create_glitch_text(args.payload)
    elif args.mode == 'zalgo':
        result = obf.create_zalgo(args.payload)
    elif args.mode == 'logo':
        result = obf.ghostbyte_logo()

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"👻 Output written to {args.output}")
    else:
        print(result)


if __name__ == '__main__':
    main()
