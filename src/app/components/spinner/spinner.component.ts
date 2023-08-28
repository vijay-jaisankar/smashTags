import { Component, ViewEncapsulation } from '@angular/core';
import { SupportService } from 'src/app/support.service';

@Component({
  selector: 'app-spinner',
  templateUrl: './spinner.component.html',
  styleUrls: ['./spinner.component.scss'],
  encapsulation: ViewEncapsulation.ShadowDom
})
export class SpinnerComponent {
  constructor(private supportService: SupportService) { }
  getLoad() {
    return this.supportService.getLoading();
  }
}
