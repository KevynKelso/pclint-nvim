" plugin/static_analysis.vim

" Register the command to load analysis results
command! LoadStaticAnalysis 
py3 << EOF
import vim
from static_analysis import load_analysis
load_analysis(vim.eval('expand("%:p")'))
EOF
