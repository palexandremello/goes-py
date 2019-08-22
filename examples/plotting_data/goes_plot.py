import numpy as np
from datetime import datetime, timedelta
from pyproj import Proj
import xarray
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
import sys
import cartopy.feature as cfeature
from cpt_convert import loadCPT # Import the CPT convert function
from matplotlib.colors import LinearSegmentedColormap # Linear interpolation for color maps

import metpy


class goes_data(object):
    """docstring for goes_data."""

    def __init__(self, filename, variable_to_plot, extent, resolution_of_plot):
        self.filename = filename
        self.x_points = None
        self.y_points = None
        self.resolution_of_plot = resolution_of_plot
        self.variable_to_plot = variable_to_plot
        self.goes_sat_data = None
        self._cmap_to_goes_plot = 'cmap_goes_sat/IR4AVHRR6.cpt'
        self._cmap_convert_cpt = None
        self._cmap = None
        self._states_provinces = None
        self._geopolitics_boundaries = None
        self.extent_of_plot = {'latmin':extent[0], 'latmax':extent[1],
                               'lonmin':extent[2], 'lonmax':extent[2]}
        self._cartopy_projection = ccrs.PlateCarree()
        self._satelite_projection = None
        self.variable_to_plot_data = None
        self.axes = None
        self.figure = None

    def _generate_shapefiles_of_plot(self):
        self._states_provinces = cfeature.NaturalEarthFeature(category='cultural', name='admin_1_states_provinces_lines',
                                                color='blue', scale='50m', facecolor='none')
        self._geopolitics_boundaries = cfeature.NaturalEarthFeature(category='cultural', name='admin_0_countries',
                                                color='blue', scale='50m', facecolor='none')
    def _generate_cmap(self):
        self._cmap_convert_cpt = loadCPT(self._cmap_to_goes_plot)
        self._cmap = LinearSegmentedColormap('cpt', cpt)

    def read_satelite_data(self):
        self.goes_sat_data = xarray.open_dataset(self.filename)

    def get_variable_to_plot(self):
        try:
            self.variable_to_plot_data = self.goes_data[self.variable_to_plot].data
            self.variable_plot_projection = self.goes_sat_data.metpy.parse_cf(self.variable_to_plot)
            self.variable_goes_to_projection = self.goes_sat_data.metpy.cartopy_crs
        except KeyError as msg:
            print("Variable name may be not correct")
            exit()

    def _get_coordinates_from_goes_satelite(self):
        self.x_points = self.variable_plot_projection.x
        self.y_points = self.variable_plot_projection.y

    def _create_cartopy_projection(self):
        self._cartopy_projection = ccrs.PlateCarre()


    def get_plot(self):
        self.figure = plt.figure(figsize=(15, 15))
        self.axes = plt.axes(projection=self._cartopy_projection)

        self.axes.set_extent([self.extent_of_plot['lonmin'], self.extent_of_plot['lonmax'],
                              self.extent_of_plot['latmin'], self.extent_of_plot['latmax']],
                              crs=self._cartopy_projection)

        self.axes.imshow(self.variable_to_plot_data[::self.resolution_of_plot, ::self.resolution_of_plot], origin='upper',
                   extent=(self.x_points.min(), self.x_points.max(), self.y_points.min(), self.y_points.max()),
                   transform=self.variable_goes_to_projection,
                   interpolation='none', cmap=self._cmap, vmin=170, vmax=378)
                   self.axes.set_title('GOES-16', loc='left', fontweight='bold')
                   self.axes.coastlines(resolution='50m', color='blue', linewidth=.75)
                   self.axes.add_feature(self._states_provinces, linewidth=.5)
                   self.axes.add_feature(self._geopolitics_boundaries, linewidth=.5)


if __name__ == '__main__':
    # rodar exemplo aqui!!
