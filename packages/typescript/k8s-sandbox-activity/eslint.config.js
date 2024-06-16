import js from '@eslint/js';
import ts from '@typescript-eslint/eslint-plugin';

import eslintPluginPrettierRecommended from 'eslint-plugin-prettier/recommended';

export default [
  {
    languageOptions: {
      ecmaVersion: 2021
    },
    rules: {
      ...js.configs.recommended.rules,
      ...ts.configs.recommended.rules,
    }
  },
];
