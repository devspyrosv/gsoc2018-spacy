# coding: utf8
from __future__ import unicode_literals
from ...symbols import ORTH, LEMMA, TAG, NORM, ADP, DET
import pickle

_exc = {

}


# norms





# abbreviations
for orth in ['χλμ.','σ.','π.μ.','μ.μ.','π.Χ.','μ.Χ.','δηλ.',
	'τ.μ.','κ.ο.κ','κ.λπ.','κ.α.','κ.ά','κ.κ','αγγλ.','λ.χ.',
	'κυβ.','κλπ.','κ.','α.α','βλ.','δισ.']:
    _exc[orth] = [{ORTH: orth}]




TOKENIZER_EXCEPTIONS = _exc
