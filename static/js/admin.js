/*global EpicEditor */

(function ($) {
	"use strict";

	$('textarea[data-provide=markdown]').each(function(index, item) {
		var $this = $(this),
			epicid = this.id+'-epiceditor',
			epiconfig = {
				container: epicid,
				basePath: '/static/epiceditor',
				clientSideStorage: false,
				file: {
					name: 'epiceditor',
					defaultContent: $this.val()
				},
				focusOnLoad: false
			},
			editor;
		
		$this.hide();
		$this.after($('<div id="'+epicid+'">'));
		editor = new EpicEditor(epiconfig);
		editor.load();
		editor.on('update', function(e) {
			$this.val(e.content);
		});

	});
}(window.jQuery));