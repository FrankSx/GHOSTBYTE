#!/usr/bin/env python3
"""
GHOSTBYTE Unicode Analyzer 👻
Analyzes text for suspicious Unicode patterns

Author: frankSx <fixes.it.frank@googlesmail.com>
13th Hour Research Division
"""

import argparse
import unicodedata
import re
from collections import defaultdict


class UnicodeAnalyzer:
    """Analyzes Unicode text for security issues - GHOSTBYTE"""

    DANGEROUS_CHARS = {
        '\u202A': 'LEFT-TO-RIGHT EMBEDDING',
        '\u202B': 'RIGHT-TO-LEFT EMBEDDING',
        '\u202C': 'POP DIRECTIONAL FORMATTING',
        '\u202D': 'LEFT-TO-RIGHT OVERRIDE',
        '\u202E': 'RIGHT-TO-LEFT OVERRIDE',
        '\u200B': 'ZERO WIDTH SPACE',
        '\u200C': 'ZERO WIDTH NON-JOINER',
        '\u200D': 'ZERO WIDTH JOINER',
        '\u200E': 'LEFT-TO-RIGHT MARK',
        '\u200F': 'RIGHT-TO-LEFT MARK',
        '\uFEFF': 'ZERO WIDTH NO-BREAK SPACE (BOM)',
    }

    HOMOGLYPH_GROUPS = [
        ['A', 'А', 'Ａ', 'Α'], ['E', 'Е', 'Ｅ', 'Ε'],
        ['O', 'О', 'Ｏ', 'Ο'], ['P', 'Р', 'Ｐ', 'Ρ'],
        ['a', 'а', 'ａ', 'α'], ['e', 'е', 'ｅ', 'ε'],
        ['o', 'о', 'ｏ', 'ο'], ['p', 'р', 'ｐ', 'ρ'],
    ]

    def analyze(self, text: str):
        """Perform full analysis of text"""
        analysis = {
            'text_sample': text[:100] + '...' if len(text) > 100 else text,
            'length': len(text),
            'byte_length': len(text.encode('utf-8')),
            'unique_chars': len(set(text)),
            'suspicious_chars': self._find_suspicious(text),
            'bidi_chars': self._find_bidi(text),
            'zero_width': self._find_zero_width(text),
            'homoglyphs': self._find_homoglyphs(text),
            'mixed_scripts': self._detect_mixed_scripts(text),
            'risk_score': 0,
            'recommendations': []
        }

        analysis['risk_score'] = self._calculate_risk(analysis)
        analysis['recommendations'] = self._generate_recommendations(analysis)

        return analysis

    def _find_suspicious(self, text: str):
        found = []
        for char in text:
            cat = unicodedata.category(char)
            if cat in ['Cc', 'Cf'] or char in self.DANGEROUS_CHARS:
                found.append({
                    'char': char,
                    'codepoint': f'U+{ord(char):04X}',
                    'name': self.DANGEROUS_CHARS.get(char, unicodedata.name(char, 'UNKNOWN')),
                    'category': cat
                })
        return found

    def _find_bidi(self, text: str):
        bidi_pattern = re.compile(r'[\u202A-\u202E]')
        found = []
        for match in bidi_pattern.finditer(text):
            char = match.group()
            found.append({
                'char': char,
                'codepoint': f'U+{ord(char):04X}',
                'name': self.DANGEROUS_CHARS.get(char, 'BIDI CONTROL'),
                'position': match.start()
            })
        return found

    def _find_zero_width(self, text: str):
        zw_pattern = re.compile(r'[\u200B-\u200F\u2060-\u2064\uFEFF]')
        found = []
        for match in zw_pattern.finditer(text):
            char = match.group()
            found.append({
                'char': repr(char),
                'codepoint': f'U+{ord(char):04X}',
                'name': self.DANGEROUS_CHARS.get(char, 'ZERO-WIDTH'),
                'position': match.start()
            })
        return found

    def _find_homoglyphs(self, text: str):
        found = []
        for i, char in enumerate(text):
            for group in self.HOMOGLYPH_GROUPS:
                if char in group and ord(char) > 127:
                    for c in group:
                        if ord(c) < 128:
                            found.append({
                                'char': char,
                                'codepoint': f'U+{ord(char):04X}',
                                'looks_like': c,
                                'position': i
                            })
                            break
        return found

    def _detect_mixed_scripts(self, text: str):
        scripts = defaultdict(list)
        for i, char in enumerate(text):
            if char.isalpha():
                codepoint = ord(char)
                if 0x0400 <= codepoint <= 0x04FF:
                    scripts['Cyrillic'].append(i)
                elif 0x0370 <= codepoint <= 0x03FF:
                    scripts['Greek'].append(i)
                elif 0xFF01 <= codepoint <= 0xFF5E:
                    scripts['Fullwidth'].append(i)

        return {
            'scripts_found': list(scripts.keys()),
            'is_mixed': len(scripts) > 1
        }

    def _calculate_risk(self, analysis: dict) -> int:
        score = 0
        score += len(analysis['suspicious_chars']) * 10
        score += len(analysis['bidi_chars']) * 15
        score += len(analysis['zero_width']) * 10
        score += len(analysis['homoglyphs']) * 8
        if analysis['mixed_scripts']['is_mixed']:
            score += 20
        return min(score, 100)

    def _generate_recommendations(self, analysis: dict):
        recs = []
        if analysis['bidi_chars']:
            recs.append("CRITICAL: Bidirectional control characters detected")
        if analysis['zero_width']:
            recs.append("WARNING: Zero-width characters present")
        if analysis['homoglyphs']:
            recs.append("WARNING: Homoglyph characters detected")
        if analysis['risk_score'] > 50:
            recs.append("HIGH RISK: Multiple suspicious patterns")
        if not recs:
            recs.append("No obvious Unicode attacks detected")
        return recs

    def generate_report(self, analysis: dict) -> str:
        lines = [
            "=" * 60,
            "👻 GHOSTBYTE UNICODE SECURITY ANALYSIS 👻",
            "=" * 60,
            f"Sample: {analysis['text_sample']}",
            f"Length: {analysis['length']} chars ({analysis['byte_length']} bytes)",
            "",
            f"RISK SCORE: {analysis['risk_score']}/100",
            "",
            "FINDINGS:",
            "-" * 40
        ]

        if analysis['bidi_chars']:
            lines.append(f"Bidirectional: {len(analysis['bidi_chars'])} found")
        if analysis['zero_width']:
            lines.append(f"Zero-Width: {len(analysis['zero_width'])} found")
        if analysis['homoglyphs']:
            lines.append(f"Homoglyphs: {len(analysis['homoglyphs'])} found")

        lines.extend(["", "RECOMMENDATIONS:", "-" * 40])
        for rec in analysis['recommendations']:
            lines.append(f"  • {rec}")

        lines.extend(["", "=" * 60, "GHOSTBYTE Analysis Complete", "=" * 60])
        return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='GHOSTBYTE Unicode Analyzer 👻')
    parser.add_argument('--text')
    parser.add_argument('--file')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--output')

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        print("👻 Error: Provide --text or --file")
        return

    analyzer = UnicodeAnalyzer()
    analysis = analyzer.analyze(text)

    if args.json:
        import json
        output = json.dumps(analysis, indent=2, ensure_ascii=False)
    else:
        output = analyzer.generate_report(analysis)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"👻 Report saved to {args.output}")
    else:
        print(output)


if __name__ == '__main__':
    main()
