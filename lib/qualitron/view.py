import revitron
from System.Collections.Generic import List


class ElementOverrides:
    """
    Class for handling graphical element overrides.
    """
    def __init__(self, view, element):
        """
        Inits a new ElementOverrids instance.

        Args:
            view (object): A Revit view element
            element (object): A Revit element or ElementId
        """
        self.overrides = revitron.DB.OverrideGraphicSettings()
        self.element = element
        self.view = view
        try:
            self.id = element.Id
        except:
            self.id = element
            

    def set(self, color, patternId, transparency=0, overrideCutPattern=True):
        """
        Sets graphical element overrides in the active view.

        Args:
            color (int): A list or tuple (r, g, b)
            pattern (object): An element id of a Revit fill pattern
            overrideCutPattern (bool, optional): Override cut pattern. Defaults to True.
        """
        patternColor = revitron.DB.Color(color[0], color[1], color[2])
        x = 0.7
        lineColor =  revitron.DB.Color(color[0] * x, color[1] * x, color[2] * x)
        self.overrides.SetSurfaceForegroundPatternColor(patternColor)
        self.overrides.SetSurfaceForegroundPatternId(patternId)
        self.overrides.SetProjectionLineColor(lineColor)
        self.overrides.SetSurfaceTransparency(transparency)
        if overrideCutPattern:
            self.overrides.SetCutForegroundPatternColor(patternColor)
            self.overrides.SetCutForegroundPatternId(patternId)
        self.view.SetElementOverrides(self.id, self.overrides)
        return self.element

    def clear(self):
        """
        Clears a graphical element overrides in view.
        """
        self.view.SetElementOverrides((self.id), self.overrides)
        return self.element


class Isolate:
    """
    Class for handling temporary isolations.
    """
    @staticmethod    
    def byCategory(categoryIds):
        """
        Isolates given categories

        Args:
            categoryIds (object): A list of category ids or a single category id
        """
        if not type(categoryIds) == list:
            categoryIds = [categoryIds]
        categoryIds = List[revitron.DB.ElementId](categoryIds)
        revitron.ACTIVE_VIEW.IsolateCategoriesTemporary(categoryIds)
    
    @staticmethod
    def byElementIds(elementIds):
        """
        Isolates given elements

        Args:
            elementIds (object): A list of element ids or a single element id
        """
        elementIds = List[revitron.DB.ElementId](elementIds)
        revitron.ACTIVE_VIEW.IsolateElementsTemporary(elementIds)