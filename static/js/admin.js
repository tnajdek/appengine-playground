/*global EpicEditor */

(function ($) {
	"use strict";

	// converts textareas to epic editors based on data-provide attribute
	$('textarea[data-provide=markdown]').each(function() {
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
				theme: {
					preview: '/../css/blog.css'
				},
				focusOnLoad: false
			},
			editor;
		
		$this.hide();
		$this.after($('<div id="'+epicid+'">'));
		editor = new EpicEditor(epiconfig);
		editor.load();
		editor.on('update', function(e) {
			$this.val(editor.exportFile());
		});

	});

	// converts input fields into automatic permalink generators based on data attributes
	$('input[data-provide=permalink]').each(function() {
		var $this = $(this),
			$title = $this.closest('form').find('input[name='+$this.data("basedOn")+']').first(),
			$parent = $this.parent();

		$this.after($('<button class="btn btn-primary"><span class="icon icon-locked"></button>'));
		$parent.on('click', 'button', function(e) {
			$(e.currentTarget).find('span.icon').first().toggleClass('icon-locked').toggleClass('icon-unlocked');
			$title.change();
			e.preventDefault();
		});
		$title.on("keyup change", function() {
			var title = $title.val(),
				re = /[^a-z0-9]+/gi,
				re2 = /^-*|-*$/g;

			if($parent.find('.icon-locked').length>0) {
				title = title.replace(re, '-');
				title = title.replace(re2, '').toLowerCase();
				$this.val(title);
			}
		});
	});
}(window.jQuery));