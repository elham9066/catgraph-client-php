import TestBase

class CoreTest (TestBase.SlaveTestBase):
    """Test core functions via client lib."""
    ## Core Functions ///////////////////////////////////////////////////////////////
    
    def testAddArcs(self):
        self.gp.add_arcs(((1, 11), (1, 12), (11, 111),(11, 112),))
        self.assertStatsValue('ArcCount', 4)
        arcs = self.gp.capture_list_successors(1)
        self.assertTrue(ConnectionTestBase.setEquals(
          arcs, ( (11), (12),)), "sucessors of (1)")
        arcs = self.gp.capture_list_successors(11)
        self.assertTrue(ConnectionTestBase.setEquals(
          arcs, ( (111), (112),)), "sucessors of (2)")

        # ------------------------------------------------------
        
        self.gp.add_arcs(( (1, 11), (11, 112), (2, 21),))
        self.assertStatsValue('ArcCount', 5)

        arcs = self.gp.capture_list_successors(2)
        self.assertTrue(
          gpConnectionTestBase.setEquals(
            arcs,((21),)),
          "sucessors of (2)" )
    
    def testClear(self):
        self.gp.add_arcs(((1, 11),(1, 12),(11, 111),(11, 112),))       
        self.assertStatsValue('ArcCount', 4)
        self.gp.clear()
        
        arcs = self.gp.capture_list_successors(1)
        self.assertEmpty(arcs)
        self.assertStatsValue('ArcCount', 0)

        #--------------------------------------------
        self.gp.add_arcs(((1, 11), (1, 12), (11, 111), (11, 112),))        
        self.assertStatsValue('ArcCount', 4)

    def testTraverseSuccessors(self):
        self.gp.add_arcs(((1, 11), (1, 12), (11, 111), ( 11, 112 ),
          (111, 1111), (111, 1112), (112, 1121),))        
        self.assertStatsValue('ArcCount', 7)
        
        #--------------------------------------------
        succ = self.gp.capture_traverse_successors(11, 5)

        self.assertEquals(((11),(111),(112),(1111),(1112),(1121),), succ)
    
    def testTraverseSuccessorsWithout(self):
        self.gp.add_arcs(((1, 11), (1, 12), (11, 111), (11, 112),
          (111, 1111), (111, 1112), (112, 1121),))        
        self.assertStatsValue('ArcCount', 7)
        
        #--------------------------------------------
        succ = self.gp.capture_traverse_successors_without(11, 5, 111, 5)
        self.assertEquals(((11), (112), (1121),), succ)

    
    #TODO: add all the tests we have in the talkback test suit
