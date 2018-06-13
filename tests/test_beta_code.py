import unittest

class TestBetaCode(unittest.TestCase):
  def test_greek_to_beta_code(self):
    self.assertEqual(
      u'xai=re w)= ko/sme',
      beta_code.greek_to_beta_code(u'χαῖρε ὦ κόσμε'),
    )

    self.assertEqual(
      u'mh=nin a)/eide qea\\ *phlhi+a/dew *)axilh=os',
      beta_code.greek_to_beta_code(u'μῆνιν ἄειδε θεὰ πηληϊάδεω ἀχιλῆος'),
    )

    self.assertEqual(
      u'kate/bhn xqe\\s ei)s *peiraia= meta\\ *glau/kwnos tou= *)ari/stwnos proseuco/meno/s te th=| qew=| kai\\ a(/ma th\\n e(orth\\n boulo/menos qea/sasqai ti/na tro/pon poih/sousin a(/te nu=n prw=ton a)/gontes. kalh\\ me\\n ou)=n moi kai\\ h( tw=n e)pixwri/wn pomph\\ e)/docen ei)=nai, ou) me/ntoi h(=tton e)fai/neto pre/pein h(\\n oi( *qra=|kes e)/pempon. proseuca/menoi de\\ kai\\ qewrh/santes a)ph=|men pro\\s to\\ a)/stu. katidw\\n ou)=n po/rrwqen h(ma=s oi)/kade w(rmhme/nous *pole/marxos o( *kefa/lou e)ke/leuse dramo/nta to\\n pai=da perimei=nai/ e( keleu=sai. kai/ mou o)/pisqen o( pai=s labo/menos tou= i(mati/ou, keleu/ei u(ma=s, e)/fh, *pole/marxos perimei=nai. kai\\ e)gw\\ metestra/fhn te kai\\ h)ro/mhn o(/pou au)to\\s ei)/h. ou(=tos, e)/fh, o)/pisqen prose/rxetai: a)lla\\ perime/nete. a)lla\\ perimenou=men, h)= d\' o(\\s o( *glau/kwn.',
      beta_code.greek_to_beta_code(u'κατέβην χθὲς εἰς πειραιᾶ μετὰ γλαύκωνος τοῦ ἀρίστωνος προσευξόμενός τε τῇ θεῷ καὶ ἅμα τὴν ἑορτὴν βουλόμενος θεάσασθαι τίνα τρόπον ποιήσουσιν ἅτε νῦν πρῶτον ἄγοντες. καλὴ μὲν οὖν μοι καὶ ἡ τῶν ἐπιχωρίων πομπὴ ἔδοξεν εἶναι, οὐ μέντοι ἧττον ἐφαίνετο πρέπειν ἣν οἱ θρᾷκες ἔπεμπον. προσευξάμενοι δὲ καὶ θεωρήσαντες ἀπῇμεν πρὸς τὸ ἄστυ. κατιδὼν οὖν πόρρωθεν ἡμᾶς οἴκαδε ὡρμημένους πολέμαρχος ὁ κεφάλου ἐκέλευσε δραμόντα τὸν παῖδα περιμεῖναί ἑ κελεῦσαι. καί μου ὄπισθεν ὁ παῖς λαβόμενος τοῦ ἱματίου, κελεύει ὑμᾶς, ἔφη, πολέμαρχος περιμεῖναι. καὶ ἐγὼ μετεστράφην τε καὶ ἠρόμην ὅπου αὐτὸς εἴη. οὗτος, ἔφη, ὄπισθεν προσέρχεται· ἀλλὰ περιμένετε. ἀλλὰ περιμενοῦμεν, ἦ δ\' ὃς ὁ γλαύκων.'),
    )

    self.assertEqual(
      u'dd*ds',
      beta_code.greek_to_beta_code(u'δδδς'),
    )

    self.assertEqual(
      u'*pollh\\ me\\n e)n brotoi=si kou)k a)nw/numos qea\\ ke/klhmai *ku/pris ou)ranou= t᾿ e)/sw:',
      beta_code.greek_to_beta_code(u'πολλὴ μὲν ἐν βροτοῖσι κοὐκ ἀνώνυμος θεὰ κέκλημαι κύπρις οὐρανοῦ τ᾿ ἔσω·'),
    )

  def test_beta_code_to_greek(self):
    self.assertEqual(
      u'χαῖρε ὦ κόσμε',
      beta_code.beta_code_to_greek(u'xai=re w)= ko/sme'),
    )

    self.assertEqual(
      u'μῆνιν ἄειδε θεὰ πηληϊάδεω ἀχιλῆος',
      beta_code.beta_code_to_greek(u'mh=nin a)/eide qea\\ *phlhi+a/dew *)axilh=os'),
    )

    self.assertEqual(
      u'κατέβην χθὲς εἰς πειραιᾶ μετὰ γλαύκωνος τοῦ ἀρίστωνος προσευξόμενός τε τῇ θεῷ καὶ ἅμα τὴν ἑορτὴν βουλόμενος θεάσασθαι τίνα τρόπον ποιήσουσιν ἅτε νῦν πρῶτον ἄγοντες. καλὴ μὲν οὖν μοι καὶ ἡ τῶν ἐπιχωρίων πομπὴ ἔδοξεν εἶναι, οὐ μέντοι ἧττον ἐφαίνετο πρέπειν ἣν οἱ θρᾷκες ἔπεμπον. προσευξάμενοι δὲ καὶ θεωρήσαντες ἀπῇμεν πρὸς τὸ ἄστυ. κατιδὼν οὖν πόρρωθεν ἡμᾶς οἴκαδε ὡρμημένους πολέμαρχος ὁ κεφάλου ἐκέλευσε δραμόντα τὸν παῖδα περιμεῖναί ἑ κελεῦσαι. καί μου ὄπισθεν ὁ παῖς λαβόμενος τοῦ ἱματίου, κελεύει ὑμᾶς, ἔφη, πολέμαρχος περιμεῖναι. καὶ ἐγὼ μετεστράφην τε καὶ ἠρόμην ὅπου αὐτὸς εἴη. οὗτος, ἔφη, ὄπισθεν προσέρχεται· ἀλλὰ περιμένετε. ἀλλὰ περιμενοῦμεν, ἦ δ\' ὃς ὁ γλαύκων.',
      beta_code.beta_code_to_greek(u'kate/bhn xqe\\s ei)s *peiraia= meta\\ *glau/kwnos tou= *)ari/stwnos proseuco/meno/s te th=| qew=| kai\\ a(/ma th\\n e(orth\\n boulo/menos qea/sasqai ti/na tro/pon poih/sousin a(/te nu=n prw=ton a)/gontes. kalh\\ me\\n ou)=n moi kai\\ h( tw=n e)pixwri/wn pomph\\ e)/docen ei)=nai, ou) me/ntoi h(=tton e)fai/neto pre/pein h(\\n oi( *qra=|kes e)/pempon. proseuca/menoi de\\ kai\\ qewrh/santes a)ph=|men pro\\s to\\ a)/stu. katidw\\n ou)=n po/rrwqen h(ma=s oi)/kade w(rmhme/nous *pole/marxos o( *kefa/lou e)ke/leuse dramo/nta to\\n pai=da perimei=nai/ e( keleu=sai. kai/ mou o)/pisqen o( pai=s labo/menos tou= i(mati/ou, keleu/ei u(ma=s, e)/fh, *pole/marxos perimei=nai. kai\\ e)gw\\ metestra/fhn te kai\\ h)ro/mhn o(/pou au)to\\s ei)/h. ou(=tos, e)/fh, o)/pisqen prose/rxetai: a)lla\\ perime/nete. a)lla\\ perimenou=men, h)= d\' o(\\s o( *glau/kwn.'),
    )

    self.assertEqual(
      u'δδδς',
      beta_code.beta_code_to_greek(u'dd*ds'),
    )

    self.assertEqual(
      u'δδδς',
      beta_code.beta_code_to_greek(u'dd*ds2'),
    )

if __name__ == '__main__':
  unittest.main()
